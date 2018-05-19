#!/usr/bin/python
#-*- coding:UTF-8 -*-
#########################################################################
# File Name: fetch_material.py
# Author: Junyi Li
# Mail: ljyduke@gmail.com
# Description:
# Created Time: 14:29:03 2018-05-19
#########################################################################
import sys

main_material = []
for line in sys.stdin:
    line = line.strip().split('\t')
    tmp = line[2].strip().split(';')
    for i in tmp:
        main_material.append(i.strip().split(',')[0])

print(','.join(main_material))
