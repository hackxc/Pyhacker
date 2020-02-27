#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import urllib3
urllib3.disable_warnings()

waf = []

def waflist():
    file = open('waf.txt')
    for line in file:
        str = line.strip().split("|")  #去除换行等字符，以|分割
        waf_data={}
        if len(str)==2: #判断是否属于waf格式
            waf_data['waf']=str[0]
            waf_data['name'] = str[1]
            waf.append(waf_data)

def wafreq(u):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        req = requests.get(url=u+'/and%201=1.php',headers=headers,verify=False,timeout=3)
        for ww in waf:
            if ww['waf'] in req.content:
                print "[+]",ww['name'],u
                f =open('Waf_url.txt','a+')
                f.write("[+]%s　%s\n"%(ww['name'],u))
                f.close()
            elif ww['waf'] in req.cookies:
                print "[+]",ww['name'],u
                f =open('Waf_url.txt','a+')
                f.write("[+]%s　%s\n"%(ww['name'],u))
                f.close()
    except:
        pass

def main():
    waflist()
    print u"\n加载waf完毕！\n"
    ff = open('url.txt','r')
    for url in ff:
        url = url.strip()
        if 'http' not in url:
            u = 'http://' + url
            wafreq(u)

if __name__ == '__main__':
    main()
