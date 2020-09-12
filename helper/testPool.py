# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      testPool.py
    @Description:    
    @Author:         
    @Date:           2020/9/12 22:37
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/12 :
"""
__author__ = 'LHY'

import multiprocessing


def a(x):
    print("num {n} is start".format(n=x))
    print(x)
    print("num {n} is end".format(n=x))


def a_2(result):
    """
    callback函数只有一个入参result, 但是可以传入多个参数，以list方式传入
    再以顺序list方式解析
    :param result:
    :return:
    """
    a, b = result
    print("num {n1} - {n2} is start".format(n1=a, n2=b))
    print(a, b)
    print("num {n1} - {n2} is end".format(n1=a, n2=b))


def b(num):
    return num


def b_2(num1, num2):
    return num1, num2


if __name__ == '__main__':
    """
    apply_async 同步非阻塞 
    多个apply_async顺序执行
    如下：
        先运行b，在运行b_2 --> next for
    """
    print("main process start")
    pool = multiprocessing.Pool()
    for i in range(5):
        pool.apply_async(b, args=[i], callback=a)

    for i in range(10):
        pool.apply_async(b_2, args=[i, i + 1], callback=a_2)
    pool.close()
    pool.join()
    print("main process end")
