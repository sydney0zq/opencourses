#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        #check type
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            #print (tds[0])
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist, num):
    print("{:^5}\t{:^9}\t{:^15}".format("排名", "学校",  "地点"))
    for i in range(num):
        u = ulist[i]
        print("{:^5}\t{:^9}\t{:^15}".format(u[0], u[1], u[2]))
        #print (u)

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


if __name__ == "__main__":
    main()

