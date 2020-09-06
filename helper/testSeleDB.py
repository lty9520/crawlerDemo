# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      testSeleDB.py
    @Description:    
    @Author:         
    @Date:           2020/9/6 22:03
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/6 :
"""
__author__ = 'LHY'

import redis
from db.dbClient import DbClient

# r = DbClient('redis://:12345@127.0.0.1:6379/0')
#pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1, password='12345')
pool = redis.ConnectionPool.from_url('redis://:12345@127.0.0.1:6379/1')
r = redis.StrictRedis(connection_pool=pool)

print(r.keys())



print("DbClient ok!")
