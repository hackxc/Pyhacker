#!/usr/bin/python
#-*- coding:utf-8 -*-

def jieguo(sql):
    global html
    html = '''
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>扫描结果</title>
    </head>
    <body>
    <center>
    </Br></Br>
    <h1>扫描结果</h1>
    </Br>
    <hr>
    %s
    </center>
    </body>
    </html>
    '''%sql

def main():
    sql = "<span style='color:red'>[+] Find sql http://127.0.0.1/news.php?id=1</span>"
    jieguo(sql)
    f = open('jieguo.html','w+')
    f.write(html)
    f.close()

if __name__ == '__main__':
    main()
    print u"Save to jieguo.html"