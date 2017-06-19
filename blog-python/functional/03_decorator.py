#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-18 Sydney <theodoruszq@gmail.com>

"""
"""

def log(func):
    def wrapper(*args, **kw):
        print ("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print ("hhh")


now()










    
