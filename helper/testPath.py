# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     testPath.py
   Description :   test os.path
   Author :       LHY
   date：          2020/08/17
-------------------------------------------------
   Change Activity:
                   2020/08/17:
-------------------------------------------------
"""
import time

__author__ = 'LHY'

import os

cur_path = os.path.dirname(os.path.abspath(__file__))
#join后的路径是简单的拼接，需要通过abspath将路径可用化
unuse_rot_path = os.path.join(cur_path, os.path.pardir)
use_rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))
down_path = os.path.join(use_rot_path, 'down')
print("cur_path" + cur_path)
print("use_rot_path" + use_rot_path)
print("unuse_rot_path" + unuse_rot_path)
print("downpath" + down_path)

print('*' * 80)

# test_join3 = os.path.join(cur_path, './test/', 'hash')
cur_data = time.strftime("%Y-%m-%d", time.localtime(time.time()))
test_join3 = os.path.abspath(os.path.join(cur_path, cur_data))
test_hash = os.path.join(test_join3, 'hash')
print(test_hash)
