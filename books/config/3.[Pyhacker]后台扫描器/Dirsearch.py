#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import urllib3
urllib3.disable_warnings()

urls = []
def dirsearch(u,dir):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
        #假的200页面进行处理
        hackxchackxchackxc = '/hackxchackxchackxc.php'
        hackxchackxchackxc_404 =requests.get(url=u+hackxchackxchackxc,headers=headers)
        # print len(hackxchackxchackxc_404.content)
        xxxxxxxxxxxx = '/xxxxxxxxxxxx'
        xxxxxxxxxxxx_404 = requests.get(url=u + xxxxxxxxxxxx, headers=headers)
        # print len(xxxxxxxxxxxx_404.content)

        #正常扫描
        req = requests.get(url=u+dir,headers=headers,timeout=3,verify=False)
        # print len(req.content)
        if req.status_code==200:
            if len(req.content)!=len(hackxchackxchackxc_404.content)and len(req.content)!= len(xxxxxxxxxxxx_404.content):
                print "[+]",req.url
                with open('success_dir.txt','a+')as f:
                    f.write(req.url+"\n")
            else:
                print u+dir,404
        else:
            print u + dir, 404
    except:
        pass

if __name__ == '__main__':
    url = raw_input('\nurl:')
    print ""
    if 'http' not in url:
        url = 'http://'+url
    dirpath = open('rar.txt','r')
    for dir in dirpath.readlines():
        dir = dir.strip()
        dirsearch(url,dir)