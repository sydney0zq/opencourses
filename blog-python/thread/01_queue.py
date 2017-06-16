#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-16 Sydney <theodoruszq@gmail.com>

"""
"""

from multiprocessing import Process, Queue
import os, time, random

# Write data
def write(q):
    print ("Process to write: %s" % os.getpid())
    for value in ['A', 'B', 'C']:
        print ("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())

# Read data
def read(q):
    print ("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print ("Get %s from queue." % value)

if __name__ == "__main__":
    # Parent create queue, and pass it to childs
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read,  args=(q,))

    pw.start()
    pr.start()
    #Wait pw to end
    pw.join()
    pr.terminate()











