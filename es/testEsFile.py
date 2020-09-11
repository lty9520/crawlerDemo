# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      testEsFile.py
    @Description:    
    @Author:         
    @Date:           2020/9/10 9:04
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/10 :
"""
import os

__author__ = 'LHY'

import filecmp
import ast

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

esClient = Elasticsearch(['localhost:9200'])


def createJson(file, jsonfile):
    """
    transform input @file to json format file @jsonfile
    replace some invalid char to valid
    最终将输出格式改为
    {"code":"codes (  '\n'  -->  null  |  '"'  -->  '\"'  |  ';'  -->  null"}
    :param file:     input origin format code file
    :param jsonfile: output json format code file
    :return:
    """

    with open(file, 'r', encoding='utf-8') as file:
        datas = file.readlines()

    j_f = open(jsonfile, "a", encoding='UTF-8')

    if os.path.getsize(jsonfile) is not True:
        # print(os.path.getsize(jsonfile))
        jsonfile_cnt = 0
    else:
        jsonfile_cnt = len(j_f.readlines())

    file_cnt = len(datas)
    if file_cnt == jsonfile_cnt:
        print("file may be not change.")
        return

    data_refor = []
    for data in datas:
        if '\n' in data:
            data = data.replace('\n', '')
        if '"' in data:
            data = data.replace('"', r'\"')
        if ';' in data:
            data = data.replace(';', '')
        if r'\\"' in data:
            data = data.replace(r'\\"', r'\"')
        data_refor.append(data)

    # ju_1 = '{"index":{"_index":"test","_id":'
    ju_2 = r'{"code":"'

    number = 1

    # print(len(datas))

    for data in data_refor:
        # res_1 = ju_1 + str(number) + '}}' + '\n'
        # print(res_1)
        # a = open(r"../out.json", "a", encoding='UTF-8')
        # a.write(res_1)

        res_2 = ju_2 + data + '"}' + '\n'
        # print(res_2)

        j_f.write(res_2)


        number +=1

    j_f.close()

    if len(data_refor) == jsonfile_cnt:
        print("create success")
    else:
        print("create failure")


'''---------------------------------------------------------------------------------------------'''


def set_data(inptfile):
    f = open(inptfile, 'r', encoding='UTF-8')
    print(f.readlines())


class ElasticObj:
    def __init__(self, index_name, ip):
        """
        :param index_name: 索引名称
        :param index_type: 索引类型
        """
        self.index_name = index_name
        # self.index_type = index_type
        # 无用户名密码状态
        self.es = Elasticsearch([ip])
        # 用户名密码状态
        # self.es = Elasticsearch([ip],http_auth=('elastic', 'password'),port=9200)

    def create_index(self):
        '''
        创建索引,创建索引名称为ott，类型为ott_type的索引
        :param ex: Elasticsearch对象
        :return:
        '''
        # 创建映射
        _index_mappings = {
            "mappings": {

                "properties": {
                    "code": {
                        'type': 'keyword',
                        'analyzer': 'ik_max_word',
                        # 'search_analyzer': 'ik_max_word'
                    }
                }

            }
        }
        if self.es.indices.exists(index=self.index_name) is not True:
            res = self.es.indices.create(index=self.index_name, body=_index_mappings, ignore=400)
            print(res)

    # 插入数据
    def insert_data(self, inputfile):
        f = open(inputfile, 'r', encoding='UTF-8')
        data = []
        for line in f.readlines():
            # 把末尾的'\n'删掉
            # print(line.strip())
            # 存入list
            data.append(line.strip())
        f.close()

        ACTIONS = []
        i = 1
        bulk_num = 2000
        for list_line in data:
            # 去掉引号，将string转为dict
            list_line = ast.literal_eval(list_line)
            action = {
                "_index": self.index_name,
                # "_type": self.index_type,  由于Elasticsearch7.x设定一个index仅有一个type，故删除该属性，否则报type过多，存入失败
                "_id": i,  # _id 也可以默认生成，不赋值
                "_source": {
                    "code": list_line["code"], # "code"为Elasticsearch中搜索的检索字段。
                    # "password": list_line["password"],
                    # "birthplace": list_line["birthplace"]
                }
            }
            i += 1
            ACTIONS.append(action)
            # 批量处理
            if len(ACTIONS) == bulk_num:
                print('插入', i / bulk_num, '批数据')
                print(len(ACTIONS))
                success, _ = bulk(self.es, ACTIONS, index=self.index_name, raise_on_error=True)
                del ACTIONS[0:len(ACTIONS)]
                print(success)

        if len(ACTIONS) > 0:
            success, _ = bulk(self.es, ACTIONS, index=self.index_name, raise_on_error=True)
            del ACTIONS[0:len(ACTIONS)]
            print('Performed %d actions' % success)


if __name__ == '__main__':
    # print("'asdasfasfa'fasfa'fasfasfa'")
    createJson("../test", "../out.json")
    #obj = ElasticObj("test_index_2", '127.0.0.1:9200')
    #obj.create_index()
    #obj.insert_data("../out.json")
    test = "../test"
    print(test + ".json")
