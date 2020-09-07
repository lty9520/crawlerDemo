# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      testMatch.py
    @Description:    
    @Author:         
    @Date:           2020/9/7 21:16
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/7 :
"""
__author__ = 'LHY'

import os

"""

    rule: 
        test:{
            corp:{
                k1:{
                    mode=1,
                    ext=js 
                }，
                k2:{
                    mode=1,
                    ext=js

"""

content_file_name = "content.txt"
cur_path = os.path.dirname(__file__)
rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))
content_path = os.path.abspath(os.path.join(rot_path, content_file_name))
with open(content_path, 'r') as f:
    contents = f.readlines()

count = 0
match_rst = {"k1": False, "k2": False, "k3": False, "k4": False, "k5": False}
idxs = []
for content in contents:
    if "bankofbeijing" in content:
        match_rst['k1'] = True
    elif "GL_DEPTH_BUFFER_BIT" in content:
        count += 1
        match_rst['k2'] = True
    elif "cpp" in content:
        match_rst['k3'] = True
    elif "hello" in content:
        match_rst['k4'] = True
    elif "test" in content:
        match_rst['k5'] = True
    else:
        continue

rst_count = 0
for k, v in match_rst.items():
    if v:
        rst_count += 1

print(rst_count)
print(match_rst)
print(count)
