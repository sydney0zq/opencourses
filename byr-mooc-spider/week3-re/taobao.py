#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\":\"[\d\.]*\"', html)
        #用到了最小匹配
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)
        for i in range(len(plt)):
            #eval能将获得的字符串中的单引号或双引号去掉
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        return ""

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print (tplt.format("index", "price", "name"))
    count = 0
    for g in ilt:
        count += 1
        print (tplt.format(count, g[0], g[1]))

def main():
    goods = "书包"
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()



