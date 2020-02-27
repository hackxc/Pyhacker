#!/usr/bin/python
#-*- coding:utf-8 -*-
import nmap

def nmapScan(host,port):
    nmScan=nmap.PortScanner()
    state = nmScan.scan(host,port)['scan'][host]['tcp'][int(port)]['state']
    print "[*] " + host + " " + port + " " + state

nmapScan('127.0.0.1','80')
