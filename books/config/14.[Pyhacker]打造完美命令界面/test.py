#!/usr/bin/python
#-*- coding:utf-8 -*-
from optparse import OptionParser

# print '''
# _                _
# | |__   __ _  ___| | ____  _____
# | '_ \ / _` |/ __| |/ /\ \/ / __|
# | | | | (_| | (__|   <  >  < (__
# |_| |_|\__,_|\___|_|\_\/_/\_\___|
#
# '''

usage = ("Usage: test.py -u target")
parser = OptionParser(usage=usage)    #实例化对象
parser.add_option('-u','--url',dest='url',help='help')  #设置参数
(options,args)=parser.parse_args()  #把参数值传递给options
url = options.url
if url == None:
    print usage


