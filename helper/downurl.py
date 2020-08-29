# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     downurl
   Description :   下载目标URL对象类型封装
   Author :        LHY
   date：          2020/8/29
-------------------------------------------------
   Change Activity:
                   2020/8/29: 下载目标URL对象类型封装
-------------------------------------------------
"""
__author__ = 'LHY'

import json

class downUrl(object):

    def __init__(self, title, down_url, down_count = 0, down_status = 1):
        self._title = title
        self._down_url = down_url
        self._down_count = down_count
        self._down_status = down_status

    @classmethod
    def createFromJson(cls, downurl_json):
        """
        根据downurl属性json创建downurl实例
        :param proxy_json:
        :return:
        """
        downurl_dict = json.loads(downurl_json)
        return cls(title = downurl_dict.get("title", ""),
                   down_url = downurl_dict.get("down_url", ""),
                   down_count = downurl_dict.get("down_count", 0),
                   down_status = downurl_dict.get("down_status", 1)
                   )
    @property
    def title(self):
        """ 下载标题 """
        return self._title

    @property
    def down_url(self):
        """ 下载url """
        return self._down_url

    @property
    def down_count(self):
        """ 总下载次数 """
        return self._down_count

    @property
    def down_status(self):
        """ 下载状态 """
        return self._down_status

    @property
    def to_dict(self):
        return {
            "title" : self._title,
            "down_url" : self._down_url,
            "down_count" : self._down_count,
            "down_status" : self._down_status
        }

    @property
    def to_json(self):
        """ 属性json格式"""
        return json.dumps(self.to_dict, ensure_ascii=False)

    # --- downurl method ---
    @title.setter
    def title(self, value):
        self._title = value

    @down_url.setter
    def down_url(self, value):
        self._down_url = value

    @down_count.setter
    def down_count(self, value):
        self._down_count = value

    @down_status.setter
    def down_status(self, value):
        self._down_status = value