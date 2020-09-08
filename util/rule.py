# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      rule.py
    @Description:    
    @Author:         
    @Date:           2020/9/7 9:14
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/7 :
"""
__author__ = 'LHY'

import json


class keyWord(object):

    def __init__(self, types, corp, kw, mode, ext):
        self._type = types
        self._corp = corp
        self._kw = kw
        self._mode = mode
        self._ext = ext

    @classmethod
    def createFromJson(cls, keyword_json):
        keyword_dict = json.loads(keyword_json)
        return cls(types=keyword_dict.get("type", "")
                   , corp=keyword_dict.get("corp", "")
                   , kw=keyword_dict.get("kw", "")
                   , mode=keyword_dict.get("mode", "normal-match")
                   , ext=keyword_dict.get("ext", "")
                   )

    @property
    def type(self):
        return self._type

    @property
    def corp(self):
        return self._corp

    @property
    def kw(self):
        return self._kw

    @property
    def mode(self):
        return self._mode

    @property
    def ext(self):
        return self._ext

    @property
    def to_dict(self):
        return {
            "type": self._type
            , "corp": self._corp
            , "kw": self._kw
            , "mode": self._mode
            , "ext": self._ext
        }

    @property
    def to_json(self):
        """json 格式属性"""
        return json.dumps(self.to_dict, ensure_ascii=False)

    # --- keyword method ---
    @type.setter
    def type(self, value):
        self._type = value

    @corp.setter
    def corp(self, value):
        self._corp = value

    @kw.setter
    def kw(self, value):
        self._kw = value

    @mode.setter
    def mode(self, value):
        self._mode = value

    @ext.setter
    def ext(self, value):
        self._ext = value
