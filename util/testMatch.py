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

rule_object = [
    {
        "types": "bankofbeijing",
        "corp_name": "bob",
        "rule_keyword": "test1",
        "mode": "normal-match",
        "ext": "js,java,py"
    },
    {
        "types": "bankofbeijing",
        "corp_name": "bob",
        "rule_keyword": "OGLES2HelloTriangle_Windows",
        "mode": "normal-match",
        "ext": "js,java,py"
    },
    {
        "types": "bankofbeijing",
        "corp_name": "bob",
        "rule_keyword": "hello",
        "mode": "normal-match",
        "ext": "js,java,py"
    },
    {
        "types": "bankofbeijing",
        "corp_name": "bob",
        "rule_keyword": "cpp",
        "mode": "normal-match",
        "ext": "js,java,py"
    },
    {
        "types": "bankofbeijing",
        "corp_name": "bob",
        "rule_keyword": "test",
        "mode": "normal-match",
        "ext": "js,java,py"
    },
]

count = 0
# match_rst = {"test1": False, "OGLES2HelloTriangle_Windows": False, "hello": False, "cpp": False, "test": False}
match_rst = {}
idxs = []
keywords = []
print(match_rst)
for rule in rule_object:
    keywords.append(rule['rule_keyword'])
for keyword in keywords:
    match_rst.__setitem__(keyword, 0)

print(match_rst)
print(keywords)
'''
for content in contents:
    # search()
    if keywords[0] in content:
        match_rst['k1'] = True
        print(keywords[0])
    # match k2 in rst of search()
    else:
        continue
    if keywords[1] in content:
        # count += 1
        match_rst['k2'] = True
        print(keywords[1])
    else:
        continue
    # match k3 in rst of search()
    if keywords[2] in content:
        match_rst['k3'] = True
        print(keywords[2])
    else:
        continue
    # match k4 in rst of search()
    if keywords[3] in content:
        match_rst['k4'] = True
        print(keywords[3])
    else:
        continue
    # match k5 in rst of search()
    if keywords[4] in content:
        match_rst['k5'] = True
        print(keywords[4])
    else:
        continue
'''

for idx, content in enumerate(contents):
    for keyword in keywords:
        if match_rst[keyword]:
            continue
        if keyword in content:
            match_rst[keyword] = idx
            # print(keyword)
            continue

rst_count = 0
for k, v in match_rst.items():
    if v:
        rst_count += 1



print(rst_count)
print(match_rst)
print(count)
