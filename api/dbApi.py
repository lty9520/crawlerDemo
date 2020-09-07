# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      dbApi.py
    @Description:    
    @Author:         
    @Date:           2020/9/7 9:01
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/7 :
"""
__author__ = 'LHY'

import platform
from werkzeug.wrappers import Response
from flask import Flask, jsonify, request

from handler.redisHandler import redisHandler
from util.keyword import keyWord
from gsil.config import get
from util.iterItem import iteritems

app = Flask(__name__)
redis_Handler = redisHandler()


class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (dict, list)):
            response = jsonify(response)

        return super(JsonResponse, cls).force_type(response, environ)


# app.response_class = JsonResponse

api_list = {
    'get_all_rule': u'get an rule'
    , 'get_rule': u'get one rule'
}


@app.route('/')
def index():
    return api_list


@app.route('/get_all_rule/')
def getAllRule():
    keyWord = redis_Handler.getAll()
    return jsonify([_.to_dict for _ in keyWord])


@app.route('/get_rule/<string:key>')
def getRule(key):
    rule = redis_Handler.getRule(key)
    # print(key)
    # print(rule)
    return rule


def runUrlFlask():
    if platform.system() == "Windows":
        app.run(host=get('server', 'serverhost'), port=get('server', 'serverport'), debug=True)
    else:
        import gunicorn.app.base

        class StandaloneApplication(gunicorn.app.base.BaseApplication):

            def __init__(self, app, options=None):
                self.options = options or {}
                self.application = app
                super(StandaloneApplication, self).__init__()

            def load_config(self):
                _config = dict([(key, value) for key, value in iteritems(self.options)
                                if key in self.cfg.settings and value is not None])
                for key, value in iteritems(_config):
                    self.cfg.set(key.lower(), value)

            def load(self):
                return self.application

        _options = {
            'bind': '%s:%s' % (get('server', 'serverhost'), get('server', 'serverport')),
            'workers': 4,
            'accesslog': '-',  # log to stdout
            'access_log_format': '%(h)s %(l)s %(t)s "%(r)s" %(s)s "%(a)s"'
        }
        StandaloneApplication(app, _options).run()


if __name__ == '__main__':
    runUrlFlask()
