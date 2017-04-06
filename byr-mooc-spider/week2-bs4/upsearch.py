#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

r = requests.get("http://python123.io/ws/demo.html")

soup = BeautifulSoup(r.text, "html.parser")

for parent in soup.a.parents:
    if parent is None:
        print (parent)
    else:
        print (parent.name)







