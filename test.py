# -*- coding:utf8 -*-
import re
f=open('C:\Users\Y\what.txt','r')
for eachline in f.readlines():
    print re.split('\s\s+',eachline)
f.close()