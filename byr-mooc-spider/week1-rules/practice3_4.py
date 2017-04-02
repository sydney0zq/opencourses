#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import requests


keyword = 'Python'
url = 'http://baidu.com/s'

try:
    kv = {'wd': keyword}
    r = requests.get(url, params = kv)
    r.raise_for_status()
    print (len(r.text))
except:
    print ("Error in baidu...")


#Save picture

import os

url = 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png'
root = '/tmp/'
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, "wb") as f:
            f.write(r.content)
            f.close()
            print ("File saved successfully...")
    else:
        print ("File existed already...")
except:
    print ("Error in getting picture...")


