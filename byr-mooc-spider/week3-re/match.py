#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import re

match = re.search(r'[1-9]\d{5}', "BIT100081 TUS200043")
if match:
    print (match.string)
    print (match.re)
    print (match.pos)
    print (match.endpos)
    print (match.group(0))
    print (match.start())
    print (match.end())
    print (match.span())


