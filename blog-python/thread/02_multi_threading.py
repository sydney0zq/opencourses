#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-18 Sydney <theodoruszq@gmail.com>

"""
"""

import time, threading

# New threading code
def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s is ended..." % threading.current_thread())

print ("thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target=loop, name="LoopThread")
t.start()
t.join()
print ("thread %s ended." % threading.current_thread().name)
