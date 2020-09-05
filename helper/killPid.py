# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     killPid.py
   Description :   kill pid
   Author :       LHY
   date：          2020/08/27
-------------------------------------------------
   Change Activity:
                   2020/08/27: killpid
-------------------------------------------------
"""
__author__ = 'LHY'

import os


def kill(pid):
    # kill 相应pid进程
    if os.name == 'nt':
        # windows
        cmd = 'taskkill /pid ' + str(pid) + ' /f'
        try:
            print (cmd)
        except Exception as e:
            print(e)

    elif os.name == 'posix':
        # linux
        cmd = 'kill ' + str(pid)
        try:
            os.system(cmd)
        except Exception as e:
            print(e)
    else:
        print('Undefined os.name')

