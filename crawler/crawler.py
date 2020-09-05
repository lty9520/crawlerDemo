# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     crawler.py
   Description :   WebApi
   Author :       LHY
   date：          2020/08/17
-------------------------------------------------
   Change Activity:
                   2020/08/17:
-------------------------------------------------
"""
__author__ = 'LHY'

import mainUtil
import getFile
import changeIP

aim_url = 'https://www.zhihu.com/question/21358581'
headers  = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}




if __name__ == '__main__':
    #mainUtil.main(headers, aim_url)
    getFile.downFile()
    #changeIP.changeIP()