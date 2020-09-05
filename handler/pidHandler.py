# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     pidHandler.py
   Description :   handle the pid of process
   Author :       LHY
   date：          2020/08/27
-------------------------------------------------
   Change Activity:
                   2020/08/27: pidHandler
-------------------------------------------------
"""
__author__ = 'LHY'

from helper.killPid import kill
import os


cur_path = os.path.dirname(os.path.abspath(__file__))
rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))


def stopServer():

    with open(rot_path + "\\pid.txt", 'r') as file:
        pid = file.readlines()

    for str_pid in pid:
        kill(str(str_pid).strip("\n"))


if __name__ == '__main__':
    stopServer()
    with open(rot_path + "\\pid.txt", 'w') as file:
        file.truncate()