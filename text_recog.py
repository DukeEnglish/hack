#!/usr/bin/python
#-*- coding:UTF-8 -*-
#########################################################################
# File Name: text_recog.py
# Author: Junyi Li
# Mail: ljyduke@gmail.com
# Created Time: 15:13:08 2018-05-02
#########################################################################
# -*- coding: utf-8 -*-
import sys
import io
import codecs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# print('哈哈哈')
#query_test = sys.argv[1]
menu = {}
f = codecs.open('menu.txt','r','utf-8')
for line in f:
    line = line.strip().split('\t')
    menu[line[0]] = line[:]

def query_search(query):
    if query in menu:
        print('\t'.join(menu[query]))
        return '\t'.join(menu[query])
    else:
        print('亲爱的同学，你请求的菜品我们暂时还没有收录，敬请期待，谢谢   ')
        return '亲ai的同学，你请求的菜品我们暂时还没有收录，敬请期待，谢谢'

#if __name__ == '__main__':
#    line = query_test
#    x = query_search(line)
#    print(x)
