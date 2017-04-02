#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import requests

url = 'http://www.ip138.com/ips138.asp?ip'

try:
    r = requests.get(url+'220.28.89.10')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("Error in ip...")


