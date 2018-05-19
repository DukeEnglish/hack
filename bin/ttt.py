#!/usr/bin/python
#-*- coding:UTF-8 -*-
#########################################################################
# File Name: ttt.py
# Author: Junyi Li
# Mail: ljyduke@gmail.com
# Description:
# Created Time: 09:59:21 2018-05-19
#########################################################################
import sys
import subprocess
import os
main = "./testmain"
if os.path.exists(main):
    rc, out = subprocess.getstatusoutput(main)
    #print ('rc = %d, \nout = %s' % (rc, out))

#print ('*'*10)
f = os.popen(main)
data = f.readlines()
f.close()
print (data)

#print ('*'*10)
os.system(main)
