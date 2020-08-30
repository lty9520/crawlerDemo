# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ProxyHandler.py
   Description :
   Author :        LHY
   date：          2020/8/29
-------------------------------------------------
   Change Activity:
                   2020/8/29:
-------------------------------------------------
"""
__author__ = 'LHY'

from helper.downurl import downUrl
from db.dbClient import DbClient
from handler.configHandler import ConfigHandler

class DownurlHandler(object):
    """ downurl CRUD operator"""

    def __init__(self):
        self.conf = ConfigHandler()
        self.db = DbClient(self.conf.dbConn)
        self.db.changeTable(self.conf.urlTableName)

    def get(self):
        """
        return a down url item
        :return:
        """
        downurl = self.db.get()
        if downurl:
            return downUrl.createFromJson(downurl)
        return None

    def pop(self):
        """
        return and delete a down url item
        :return:
        """
        downurl = self.db.pop()
        if downurl:
            return downUrl.createFromJson(downurl)
        return None

    def put(self, downurl):
        """
        put a down url item
        :param downurl: down utl item
        :return:
        """
        self.db.put(downurl)

    def delete(self, downurl):
        """
        delete a down url item
        :param downurl: down url item
        :return:
        """
        return self.db.delete(downurl.title)

    def getAll(self):
        """
        get all down url from db as list
        :return:
        """
        down_dict =self.db.getAll()
        return [downUrl.createFromJson(value) for _, value in down_dict.items()]

    def exists(self, downurl):
        """
        check down url item exists
        :param downurl:
        :return:
        """
        return self.db.exists(downurl.title)

    def getCount(self):
        """
        return down url count
        :return:
        """
        total_down_url = self.db.getCount()
        return {'count' : total_down_url}