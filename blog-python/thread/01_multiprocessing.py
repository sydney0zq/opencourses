#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-16 Sydney <theodoruszq@gmail.com>

"""
"""

from multiprocessing import Process
import os

# Code to be run for child
def run_proc(name):
    print ("Run child process %s (%s)" % (name, os.getpid()))

if __name__ == "__main__":
    print ("Parent process %s." % os.getpid())
    p = Process(target = run_proc, args=("test",))
    print ("Child process will start")
    p.start()
    p.join()
    print ("Child process ends.")
