#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-16 Sydney <theodoruszq@gmail.com>

"""
"""

import subprocess

print ("$ nslookup")
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b"set q=mx\npython.org\nexit\n")
print (output.decode("utf-8"))
print ("Exit code: ", p.returncode)
