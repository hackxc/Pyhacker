#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re

urls = []
url_ok = []
url_bing=[]

def req(q,first):
    global html
    url = 'https://cn.bing.com/search?q=%s&first=%s'%(q,first)
    print url
    headers = {
        'Host':'cn.bing.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
        'Cookie': '_EDGE_V=1;'
    }
    req = requests.get(url,headers=headers)
    html = req.content

def reurl():#正则匹配url
    urlr = r'target="_blank" href="(http.*?\..*?\..*?)" h="'
    reurl = re.findall(urlr,html)
    for url in reurl:
        if url not in urls:
            urls.append(url)

def url():#url二次处理
    for url in urls:
        urlr = r'(http[s]?://.*?)/'
        url = re.findall(urlr,url)
        url_ok.append(url[0])

def qc():#去重复
    for url in url_ok:
        if url in url_bing:
            continue
        url_bing.append(url)

if __name__ == '__main__':
    q = raw_input('\nkey:')
    page = input('page:')
    for first in range(0, page):
        req(q, first * 10)
        reurl()
    url()
    qc()
    with open('url_bing.txt','a+')as f:
        for url in url_bing:
            print url
            f.write(url+"\n")
        print "Save as url_bing.txt"