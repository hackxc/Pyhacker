#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Charset':'c3lzdGVtKCJlY2hvIHhjNjY2YSIpOw==',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'close',
            }

def phpstudy(url):
    try:
        if 'http' not in url:
            url = 'http://' + url
        r = requests.get(url=url, headers=headers,timeout=5)
        if 'xc666' in r.text:
            print u'over success：',url
            with open('success.txt','a+') as f:
                f.write(url+"\n")
        else:
            print u'flase：',url
    except:
        print u'连接超时',url

if __name__ == '__main__':
    url = raw_input('\nurl:')
    phpstudy(url)