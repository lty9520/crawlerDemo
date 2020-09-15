# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      testBlack.py
    @Description:    
    @Author:         
    @Date:           2020/9/11 17:16
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/11 :
"""
__author__ = 'LHY'

import os
from github import Github

with open("../black", 'r') as f:
    blacks = f.readlines()

g = Github(login_or_token='5aa43a150bc7527f566a27952ec42b8b9de14d49', per_page=50)

print(blacks.__len__())

test = [11, 22]

for idx, black in enumerate(blacks):
    # print(num)
    repo_query = ''
    repo_kw = black.split(' ')
    repo_query += '{keyword} repo:{r} '.format(keyword=repo_kw[1].strip(), r=repo_kw[0].strip())

    print(repo_query)

    resource = g.search_code(repo_query, sort='indexed', order='desc')

    pages = 1
    for page in range(pages):
        page_content = resource.get_page(page)
        for index, content in enumerate(page_content):
            code = content.decoded_content.decode('utf-8')
            print("***************index : " + str(index) + "**************")
            print("code : " + code)

# keyword = "connectionpool repo:lty9520/crawlerDemo"



# print(resource)

