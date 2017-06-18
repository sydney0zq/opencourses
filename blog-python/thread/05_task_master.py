#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-18 Sydney <theodoruszq@gmail.com>

"""
"""

import random, time, queue
from multiprocessing.managers import BaseManager

# Queue for sending tasks
task_queue = queue.Queue()
# Queue for receiving tasks
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

# Put two Queues on network
QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)

# Bind port 5000, set passcode 'abc'
manager = QueueManager(address=('', 5000), authkey=b"abc")
# Start queue
manager.start()
# Get queue object from network
task = manager.get_task_queue()
result = manager.get_result_queue()

# Put several tasks into it
for i in range(10):
    n = random.randint(0, 10000)
    print("Put task %d..." % n)
    task.put(n)

# Read result in result queue
print("Try get results...")
for i in range(10):
    r = result.get(timeout=10)
    print("Result: %s" % r)

# Close
manager.shutdown()
print("Master exit...")

