#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
import urllib3
urllib3.disable_warnings()

url_s = []

def depth(url,who):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
        req = requests.get(url=url,headers=headers,timeout=3,verify=False)
        r = r'href="(.*?)"'
        urls = re.findall(r,req.content)
        for url in urls:
            if who in url:
                if url not in url_s:
                    if 'css' not in url :
                        url_s.append(url)
    except:
        pass

def main():
    url =raw_input('\nurl:')
    #取域名部分
    r = url.split('.')
    who = r[-2]+"."+r[-1]
    if 'http' not in url:
        url = 'http://'+url
    depth(url,who)
    print u"\n采集到了%s url"%len(url_s)

    while True:
        print u"\n开始执行深度采集"
        for url in url_s:
            if 'http' not in url:
                url = 'http://' + url
            depth(url,who)
            print url
        if len(url_s)==len(url_s):
            break

if __name__ == '__main__':
    main()
    print u"\n采集完成"
    print u"\n采集到了%surl"%len(url_s)
    with open('Url_depth.txt','a+')as f:
        for url in url_s:
            f.write(url+"\n")
    print "\nSave the url_depth.txt!!!"