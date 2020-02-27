#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import subprocess

# os.system('whoami') #cmd
#
# args = [r"powershell", r"whoami"]    #调出powershell，后面是执行的命令
# subprocess.call(args)
#
# subprocess.call('whoami') #cmd

args = [r"arp", r"-a"]    #命令拼接
subprocess.call(args)