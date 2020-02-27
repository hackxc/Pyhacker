#!/usr/bin/python
#-*- coding:utf-8 -*-
import socket
import ipaddr

def portscan(ip,port):
    sockect = socket.socket()
    try:
        sockect.settimeout(0.2)
        sockect.connect((ip,port))
        print "[+]%s open %s"%(ip,port)
    except:
        sockect.close()

portlist = [21,80,443,445,3306,27017,6379]
if __name__ == '__main__':
    ip = raw_input('\nIP:')
    print ""
    ips = ipaddr.IPNetwork(ip)
    for ip in ips:
        for port in portlist:
            portscan(str(ip),port)
