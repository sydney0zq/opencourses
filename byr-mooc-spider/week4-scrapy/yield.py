#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy an "if/else" anymore.
"""

def gen(n):
    print("outside")
    for i in range(8):
        print ("inside")
        yield i ** 2

for i in gen(5):
    print (i, " ")

print ("*" * 50)

def gen2(n):
    print("outside")
    for i in range(n):
        print ("inside")
        yield i ** 2

n = 3
for i in gen2(n):
    #n = 10     this statement does NO effect 
    print (i)

print ("*" * 50)

def square(n):
    print ("inside")
    ls = [i**2 for i in range(n)]
    return ls

for i in square(5):
    print(i)




