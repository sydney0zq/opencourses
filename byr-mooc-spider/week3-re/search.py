#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import re

match = re.search(r'[1-9]\d{5}', "BIT100081")
if match:
    print(match.group(0))
    print(match)

print ("*" * 20)

#从一个字符串的开始位置起匹配正则表达式，返回match对象
match = re.match(r'[1-9]\d{5}', "10000111BIT100081")
if match:
    print(match.group(0))


print ("*" * 20)
match = re.findall(r'[1-9]\d{5}', "BIT100081 TSU100084")

if match:
    print(match)


print ("*" * 20)
match = re.split(r'[1-9]\d{5}', "BIT100081 TSU100084", maxsplit = 1)

if match:
    print(match)

print ("*" * 20)
match = re.finditer(r'[1-9]\d{5}', "BIT100081 TSU100084")

for m in match:
    if m:
        print(m.group(0))

print ("*" * 20)
match = re.sub(r'[1-9]\d{5}', ':zipcode', "BIT100081 TSU100084")

if match:
    print(match)



