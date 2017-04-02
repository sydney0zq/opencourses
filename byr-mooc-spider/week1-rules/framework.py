#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=10)
        #If status_code is not 200, raise HTTPError
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error happened..."

if __name__ == '__main__':
    url = "http://baidu.com"
    print(getHTMLText(url))



