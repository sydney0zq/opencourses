#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-06-18 Sydney <theodoruszq@gmail.com>

"""
"""

class Student(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age')

class GraduateStudent(Student):
    pass

s = Student()   # Create a new instance
s.name = "Michael"
s.age = 25
try:
    s.score = 99
except AttributeError as e:
    print ("AttributeError:", e)

g = GraduateStudent()
g.score = 99
print ("g.score is ", g.score)
