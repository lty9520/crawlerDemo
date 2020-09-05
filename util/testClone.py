# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      testClone.py
    @Description:    
    @Author:         
    @Date:           2020/9/5 14:04
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/5 :
"""
__author__ = 'LHY'

from github import Github
from git.repo import Repo
import os

cur_path = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(cur_path, os.path.pardir))
g = Github("b077ee68a810d3a5b8eb0c9e86c0360c80f8aef2"
           , user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
           )

i = 0


def getContents(i):
    print(i)
    i += 1
    try:
        rate = g.get_rate_limit()
    except ConnectionResetError as e:
        getContents(i)
    print("rate_limit : " + str(rate))
    # g = Github("lty9520", "Liuhaoyu110")
    repo = g.get_repo("lty9520/XML2InfoGraph")
    return repo.get_contents("")


contents = getContents(i)
for content_file in contents:
    print(content_file)

# print(repo.git_url)
# print(repo.clone_url)

# clone_path = os.path.join(path, str(repo.id))
# Repo.clone_from(repo.html_url, to_path=clone_path)


