# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     testKill.py
   Description :   testKill
   Author :       LHY
   date：          2020/08/27
-------------------------------------------------
   Change Activity:
                   2020/08/27: testKill
-------------------------------------------------
"""
__author__ = 'LHY'

from helper import killPid
import os

pids = ['123124', '12312', '3463', '3747']


cur_path = os.path.dirname(os.path.abspath(__file__))
rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))

def openTest():
    file = open(rot_path + "\\pid.txt", 'r')
    pid = file.readlines()

    for str_pid in pid:
        str1 = str(str_pid).strip("\n")
        print(str1)






def writeTest():
    with open(rot_path + "\\pid.txt", 'a') as file:
        for a in pids:
            file.write(a)
            file.write("\n")



if __name__ == '__main__':
    writeTest()
    openTest()
    with open(rot_path + "\\pid.txt", 'w') as file:
        file.truncate()
