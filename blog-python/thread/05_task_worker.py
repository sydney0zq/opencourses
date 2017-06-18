#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-18 Sydney <theodoruszq@gmail.com>

"""
"""

import time, sys, queue
from multiprocessing.managers import BaseManager

# Create similar QueueManager
class QueueManager(BaseManager):
    pass

# We just supply names since we get Queue from internet
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

# Connect to the server which runs task_master.py
server_addr = "127.0.0.1"
print ("connect to server %s..." % server_addr)
# Auth
m = QueueManager(address=(server_addr, 5000), authkey=b"abc")
# Connect from network
m.connect()
# Get the Queue object
task = m.get_task_queue()
result = m.get_result_queue()

# Get tasks from task queue, and write results to result queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        print("run task %d * %d" % (n, n))
        r = "%d * %d = %d" % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print("task queue is empty...")
# Over
print ("Work exit...")
