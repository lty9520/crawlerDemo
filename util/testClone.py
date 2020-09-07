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
import time

__author__ = 'LHY'

from github import Github
from git.repo import Repo
import os

cur_path = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(cur_path, os.path.pardir))
g = Github("8f414d261219a9bb2b4f1e06042dc28696610dde"
           , user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
           )

i = 0



def getContents(i):
    print(i)
    i += 1
    try:
        rate = g.rate_limiting_resettime
    except ConnectionResetError as e:
        getContents(i)
    print("rate_limit : " + str(rate))
    # g = Github("lty9520", "Liuhaoyu110")
    repo = g.get_repo("lty9520/XML2InfoGraph")
    # return repo.get_contents("")
    # return rate
    return repo


contents = getContents(i)
# for content_file in contents:
#     print(content_file)

#rate_reset = getContents(i)
#print("ratetime-reset : " + str(rate_reset))
print("time now : " + time.strftime('%Y-%m-%d', time.localtime(time.time())))
# print("time now : " + '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#print("ratetime2time : " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(rate_reset)))

log_path = 'logs'
cur_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
if os.path.isdir(os.path.abspath(os.path.join(log_path, cur_date))) is not True:
    log_path = os.path.abspath(os.path.join(log_path, cur_date))
    os.mkdir(log_path, 0o755)



# print(repo.git_url)
# print(repo.clone_url)

repo = getContents(i)
clone_path = os.path.join(path, str(repo.id))
Repo.clone_from(repo.html_url, to_path=clone_path)


