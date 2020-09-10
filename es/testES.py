# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      testES.py
    @Description:    
    @Author:         
    @Date:           2020/9/9 21:26
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/9 :
"""
__author__ = 'LHY'

from elasticsearch import Elasticsearch

esClient = Elasticsearch(['localhost:9200'])
response = esClient.search(
    index='social-*',
    body={
        "query": {
            "match_all": {

            }
        }

    }
)

print(response)
