#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-16 Sydney <theodoruszq@gmail.com>

"""
"""

import os

print("Process (%s) start..." % os.getpid())
# Only works on Unix/Linux/Mac
pid = os.fork()
if pid == 0:
    print("I am child process (%s) and my parent is %s." % (os.getpid(), os.getppid()))
else:
    print("I (%s) just created a child process (%s)." % (os.getpid(), pid))
