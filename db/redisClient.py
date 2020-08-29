# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
   File Name：     redisClient.py
   Description :   封装Redis相关操作
   Origin Author :   JHao
   Modify Author :   LHY
   date：          2019/8/9
------------------------------------------------------
   Change Activity:
                   2019/08/09: 封装Redis相关操作
                   2020/06/23: 优化pop方法, 改用hscan命令
                   2020/08/29: 增加部分URL方法
------------------------------------------------------
"""
__author__ = 'JHao'

from redis.connection import BlockingConnectionPool
from random import choice
from redis import Redis


class RedisClient(object):
    """
    Redis client

    Redis中代理存放的结构为hash：
    key为ip:port, value为代理属性的字典;

    """

    def __init__(self, **kwargs):
        """
        init
        :param host: host
        :param port: port
        :param password: password
        :param db: db
        :return:
        """
        self.name = ""
        kwargs.pop("username")
        self.__conn = Redis(connection_pool=BlockingConnectionPool(decode_responses=True, **kwargs))

    def get(self):
        """
        返回一个代理
        :return:
        """
        proxies = self.__conn.hkeys(self.name)
        proxy = choice(proxies) if proxies else None
        if proxy:
            return self.__conn.hget(self.name, proxy)
        else:
            return False

    def getdownUrl(self):
        """
        返回一个下载链接
        :return:
        """
        downurls = self.__conn.hkeys(self.name)
        downurl = choice(downurls) if downurls else None
        if downurl:
            return self.__conn.hget(self.name, downurl)
        else:
            return False

    def put(self, proxy_obj):
        """
        将代理放入hash, 使用changeTable指定hash name
        :param proxy_obj: Proxy obj
        :return:
        """
        data = self.__conn.hset(self.name, proxy_obj.proxy, proxy_obj.to_json)
        return data

    def putUrl(self, downurl_obj):
        """
        将URL放入hash， 使用changeTable制定hash name
        :param downurl_obj: downUrl obj
        :return:
        """
        url_data = self.__conn.hset(self.name, downurl_obj.title, downurl_obj.to_json)
        return url_data

    def pop(self):
        """
        弹出一个代理
        :return: dict {proxy: value}
        """
        proxies = self.__conn.hkeys(self.name)
        for proxy in proxies:
            proxy_info = self.__conn.hget(self.name, proxy)
            self.__conn.hdel(self.name, proxy)
            return proxy_info
        else:
            return False

    def popUrl(self):
        """
        弹出一个uRL
        :return: dict {downurl : value}
        """
        downurls = self.__conn.hkeys(self.name)
        for downurl in downurls:
            downurl_info = self.__conn.hget(self.name, downurl)
            self.__conn.hdel(self.name, downurl)
            return downurl_info
        else:
            return False

    def delete(self, proxy_str):
        """
        移除指定代理, 使用changeTable指定hash name
        :param proxy_str: proxy str
        :return:
        """
        return self.__conn.hdel(self.name, proxy_str)

    def deleteUrl(self, url_str):
        """
        移除制定URL， 使用changeTable制定hash name
        :param url_str: url str
        :return:
        """
        return self.__conn.hdel(self.name, url_str)

    def exists(self, proxy_str):
        """
        判断指定代理是否存在, 使用changeTable指定hash name
        :param proxy_str: proxy str
        :return:
        """
        return self.__conn.hexists(self.name, proxy_str)

    def existsUrl(self, url_str):
        """
        判断制定url是否存在， 使用changeTable指定hash name
        :param url_str:
        :return:
        """
        return self.__conn.hexists(self.name, url_str)

    def update(self, proxy_obj):
        """
        更新 proxy 属性
        :param proxy_obj:
        :return:
        """
        return self.__conn.hset(self.name, proxy_obj.proxy, proxy_obj.to_json)

    def updateUrl(self, downurl_obj):
        """
        更新url属性
        :param downurl_obj:
        :return:
        """
        return self.__conn.hset(self.name, downurl_obj.title, downurl_obj.to_json)

    def getAll(self):
        """
        字典形式返回所有代理, 使用changeTable指定hash name
        :return:
        """
        item_dict = self.__conn.hgetall(self.name)
        return item_dict

    def clear(self):
        """
        清空所有代理, 使用changeTable指定hash name
        :return:
        """
        return self.__conn.delete(self.name)

    def getCount(self):
        """
        返回代理数量
        :return:
        """
        return self.__conn.hlen(self.name)

    def changeTable(self, name):
        """
        切换操作对象
        :param name:
        :return:
        """
        self.name = name
