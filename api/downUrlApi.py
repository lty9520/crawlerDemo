# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     downUrlApi.py
   Description :   WebApi
   Author :       LHY
   date：          2020/08/29
-------------------------------------------------
   Change Activity:
                   2020/08/29: WebApi
-------------------------------------------------
"""
__author__ = 'LHY'

import platform
from werkzeug.wrappers import Response
from flask import Flask, jsonify, request

from util.six import iteritems
from handler.downurlHandler import DownurlHandler
from handler.configHandler import ConfigHandler
from helper.downurl import downUrl

app = Flask(__name__)
conf = ConfigHandler()
downurl_handler = DownurlHandler()

class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (dict, list)):
            response = jsonify(response)

        return super(JsonResponse, cls).force_type(response, environ)


app.response_class = JsonResponse

api_list = {
    'getUrl' : u'get an url',
    'popUrl' : u'get and delete an url',
    'get_all_Url' : u'get all urls from db',
    'delete_Url?title=ABC' : u'delete an url',
    'get_count_Url' : u'urls number'
}

@app.route('/')
def index():
    return api_list

@app.route('/getUrl/')
def getUrl():
    downurl = downurl_handler.get()
    return downurl.to_dict if downurl else {"code" : 0, "src" : "no url"}

@app.route('/popUrl/')
def popUrl():
    downurl = downurl_handler.pop()
    return downurl.to_dict if downurl else {"code" : 0, "src" : "no url"}

@app.route('/get_all_Url/')
def getAllUrl():
    downurls = downurl_handler.getAll()
    return jsonify([_.to_dict for _ in downurls])

@app.route('/delete_Url/', methods=['GET'])
def deleteUrl():
    downurl = request.args.get('title')
    status = downurl_handler.delete(downUrl(downurl))
    return {"code" : 0, "src" : status}

@app.route('/get_count_Url/')
def getCountUrl():
    status = downurl_handler.getCount()
    return status

def runUrlFlask():
    if platform.system() == "Windows":
        app.run(host=conf.serverHost, port=conf.urlServerPort)
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
            'bind': '%s:%s' % (conf.serverHost, conf.serverPort),
            'workers': 4,
            'accesslog': '-',  # log to stdout
            'access_log_format': '%(h)s %(l)s %(t)s "%(r)s" %(s)s "%(a)s"'
        }
        StandaloneApplication(app, _options).run()


if __name__ == '__main__':
    runUrlFlask()