#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-18 Sydney <theodoruszq@gmail.com>

"""
"""

import threading

# Create global ThreadLocal object
local_school = threading.local()

def process_student():
    # Get the student object associated with current thread
    std = local_school.student
    print ("hello, %s (in %s)" % (std, threading.current_thread().name))

def process_thread(name):
    # Bind studnet object of ThreadLocal
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=("Alice",), name="ThreadA")
t2 = threading.Thread(target=process_thread, args=("Bob",), name="ThreadB")

t1.start()
t2.start()
t1.join()
t2.join()
