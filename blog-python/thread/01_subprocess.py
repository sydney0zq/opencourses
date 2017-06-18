#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-16 Sydney <theodoruszq@gmail.com>

"""
"""

import subprocess

print ("$ nslookup www.python.org")
r = subprocess.call(["nslookup", "www.python.org"])
print ("Exit code: ", r)
