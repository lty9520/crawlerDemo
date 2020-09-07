# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      testReadRule.py
    @Description:    
    @Author:         
    @Date:           2020/9/7 13:00
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/7 :
"""
__author__ = 'LHY'

import redis
import json
import os

cur_path = os.path.dirname(__file__)
home_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))
code_path = os.path.join(home_path, 'code')
project_directory = os.path.abspath(os.path.join(cur_path, os.pardir))
config_path = os.path.join(project_directory, 'config.gsil')
rules_path = os.path.join(project_directory, 'rules.gsil')


pool = redis.ConnectionPool.from_url('redis://:12345@127.0.0.1:6379/1')
r = redis.StrictRedis(connection_pool=pool)

rules_dict = eval(str(r.hget("keyword", "test1"), 'utf-8'))
print(rules_dict)

with open(rules_path) as f:
    rules_dict = json.load(f)


class Rule(object):
    def __init__(self, types=None, corp=None, keyword=None, mode='normal-match', extension=None):
        self.types = types
        self.corp = corp
        self.keyword = keyword
        self.mode = mode
        self.extension = extension


def get_rules_redis(rule_types):
    if ',' in rule_types:
        rule_types = rule_types.split(',')
    else:
        rule_types = [rule_types]
    rules_objects = []
    for type in rule_types:
        if type in rule_types:
            rule_dict = r.hget("keyword", type)
            rule_keyword, rule_mode = rule_dict.get("kw"), rule_dict.get("mode")
            if ' ' in rule_keyword:
                rule_keyword, rule_mode = rule_keyword.split(''), rule_mode.split(' ')
            else:
                rule_keyword, rule_mode = [rule_keyword], [rule_mode]
            for kw, mo in rule_keyword, rule_mode:
                keyword = kw.strip()
                corp_name = rule_dict.get("corp")


def get_rules(rule_types):
    if ',' in rule_types:
        rule_types = rule_types.split(',')
    else:
        rule_types = [rule_types]
    rules_objects = []
    for types, rule_list in rules_dict.items():
        # 仅选择指定的规则类型
        if types in rule_types:
            for corp_name, corp_rules in rule_list.items():
                for rule_keyword, rule_attr in corp_rules.items():
                    rule_keyword = rule_keyword.strip()
                    corp_name = corp_name.strip()
                    types = types.upper()
                    if 'mode' in rule_attr:
                        mode = rule_attr['mode'].strip().lower()
                    else:
                        # 默认匹配模式
                        mode = 'normal-match'
                    if 'ext' in rule_attr:
                        extension = rule_attr['ext'].strip()
                    else:
                        # 默认为空
                        extension = None
                    rl = Rule(types, corp_name, rule_keyword, mode, extension)
                    rules_objects.append(rl)
    return rules_objects


def get_rule_types():
    types = []
    for k, v in rules_dict.items():
        types.append(k.upper())
    return types


def get_rule_corps():
    corps = []
    for k, v in rules_dict.items():
        for k2, v2 in v.items():
            corps.append(k2)
    return corps


if __name__ == '__main__':
    rule_obj = get_rules("test")
    # print(rule_obj)
