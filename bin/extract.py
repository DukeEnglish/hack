#!/usr/bin/python
#-*- coding:UTF-8 -*-
#########################################################################
# File Name: extract.py
# Author: Junyi Li
# Mail: ljyduke@gmail.com
# Description:
# Created Time: 10:18:12 2018-05-19
#########################################################################
import sys

out=set()
for line in sys.stdin:
    line = line.strip().split('\t')
    materials = line[2].strip().split(';') 
    for i in materials:
        i = i.strip().split(',')
        out.add(i[0].strip())

print(','.join(list(out)))
