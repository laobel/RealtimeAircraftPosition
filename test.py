#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from datetime import datetime
import json

""" 
@author:WLBDEVELOP 
@file: test.py 
@time: 2019/05/28 
"""


# python实现递归的二分查找算法
def find(li, key, value):
    p = len(li) - 1
    while p >= 0:
        if li[p][key] == value:
            return p
        p -= 1
    return -1


data = []
f = open("test.txt")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
start = datetime.now()
while line:
    now = datetime.now()

    d = eval(line)
    i = find(data, 'icao', d['icao'])
    if i >= 0:
        data[i] = d
    else:
        data.append(d)

    if (now - start).microseconds >= 0.5:
        print(data)
        data = []
        start = now

    line = f.readline()

f.close()
