#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import hashlib
import sys

data=[]
def cmslist():
    file = open(r"cms.txt")
    for line in file:
        str = line.strip().split("|")
        ls_data={}
        if len(str)==3:#判断是否为正确cms格式
            ls_data['url']=str[0]
            ls_data['name'] = str[1]
            ls_data['md5'] = str[2]
            data.append(ls_data)
    file.close( )

def cms(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
    for cms in data:
        urlx = url+cms['url']
        try:
            req = requests.get(urlx,headers=headers,timeout=2)
            print urlx
        except:
            pass
        try:
            if req.status_code == 200:
                filemd5 = hashlib.md5(req.content).hexdigest()
                if filemd5 == cms['md5']:
                    print '\n[*]cms:',cms['name']
                    break
        except:
            pass

def main():
    cmslist()
    url =raw_input("\nurl:")
    if url == "":
        sys.exit(1)
    print ""
    if 'http' not in url:
        url = 'http://'+url
    cms(url)

if __name__ == '__main__':
    main()
