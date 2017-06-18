#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-18 Sydney <theodoruszq@gmail.com>

"""
"""

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print ("%s: %s" % (self.name, self.score))
    def get_level(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"

bart = Student("Bart Ass", 70)
lisa = Student("Ali Adam", 55)

bart.print_score()
lisa.print_score()
print (bart.get_level())
print (lisa.get_level())

