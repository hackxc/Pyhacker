#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests,re

def demo(qq):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://api.oioweb.cn/api/Membereq.php?qq=%s'%qq
    req = requests.get(url,headers=headers)
    html = req.json()
    print u"开通业务如下："
    for x in html['data']['name']:
        print x

if __name__ == '__main__':
    url = raw_input("\nQQ:")
    print u"正在查询，请稍后...\n"
    demo(url)