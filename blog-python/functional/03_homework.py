#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-18 Sydney <theodoruszq@gmail.com>

"""
"""

import functools

def pad(text=None):
    if hasattr(text, '__call__'):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print ("Begin %s %s()" % (text, func.__name__))
                func(*args, **kw)
                print ("End %s %s()" % (text, func.__name__))
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print ("Begin Call %s(): " % (text.__name__))
            text(*args, **kw)
            print ("End Call %s(): " % (text.__name__))
        return wrapper


@pad("execute")
def p(inp):
    print ("body")

p("a")
