# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      retuTupTest.py
    @Description:    
    @Author:         
    @Date:           2020/9/8 13:28
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/8 :
"""
__author__ = 'LHY'

tup = ("111", True, "test", 2000)
flag = False


def testReturn(a, b):
    if flag:
        return a, b
    else:
        return False, b, a


class myClass():
    def __init__(self):
        self.test = 1

    def add(self):
        self.test += 1



if testReturn(1, 2):
    print("t")
else:
    print("f")

cl = myClass()
if flag:
    cl.add()
    if 1:
        print(cl.test)
else:
    print(cl.test)

print("123" + str(myClass().test))

print(tup)

print('-' * 20)
test = ['1', '2', '3']
for t in test[1:3]:
    print(t)

class Rule(object):
    def __init__(self, types=None, corp=None, keyword=None, mode='normal-match', extension=None):
        self.types = types
        self.corp = corp
        self.keyword = keyword
        self.mode = mode
        self.extension = extension

print('-' * 20)

rules = [
    Rule("type", "corp", "kw", "mode", "ext")
]

print(rules)