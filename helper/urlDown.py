import os
import random

import requests
from handler.configHandler import ConfigHandler
from util.webRequest import WebRequest
from helper.scheduler import runProxyCheck

conf = ConfigHandler()
webRe = WebRequest()


def getProxyIP():
    """
    随机获取一个ip
    :return:
    """
    return requests.get("http://" + str(conf.serverHost) + ":" + str(conf.serverPort) + "/get/").json()


def delProxyIP(proxy):
    """
    删除不可用IP
    :param proxy: 不可用ip
    :return:
    """
    requests.get("http://" + str(conf.serverHost) + ":" + str(conf.serverPort) + "/delete/?proxy={}".format(proxy))


def getProxyNum():
    """
    获取数据库中的ip总数(bytes格式）   eval（bytes) 转换成字典['count'] 取值
    :return:
    """
    return eval(requests.get("http://" + str(conf.serverHost) + ":" + str(conf.serverPort) + "/get_status/").content)[
        'count']


def getUrl():
    """
    随机获取一个url
    :return:
    """
    return requests.get("http://" + str(conf.serverHost) + ":" + str(conf.urlServerPort) + "/getUrl/").json()


def getUrlCount():
    """
    获取url数量
    :return:
    """
    return requests.get(
        "http://" + str(conf.serverHost) + ":" + str(conf.urlServerPort) + "/get_count_Url/").json().get("count")


def getAllUrls():
    """
    获取所有urls
    :return:
    """
    return requests.get("http://" + str(conf.serverHost) + ":" + str(conf.urlServerPort) + "/get_all_Url/").json()


def getRes(url, proxy):
    """
    获取Response
    :return:
    """
    headers = {
        'User-Agent': webRe.user_agent
    }

    # cookies KV style

    cookies = {
        "_ga": "GA1.2.674636311.1596542605",
        "cirgu": "_1_lQW3CauilVNWfPtDsrnQ542KhXCaSTVRqjirTFiMwrSIKx3U0HMoVeEVHNcJf1uohw%3D%3D",
        "_gid": "GA1.2.859316147.1598277611"
    }

    # urlNum = getUrlCount()

    # proxyNum = getProxyNum()

    proxy = {
        "http": "http://{}".format(proxy),
        #"https": "https://{}".format(proxy)
    }

    # 发起请求，获取二进制数据
    re = requests.get(url, headers=headers
                      # , cookies=cookies
                      , proxies=proxy
                      )

    return re


def downFile():
    runProxyCheck()

    url_obj = getUrl()
    url = url_obj.get("down_url")
    url_title = url_obj.get("title")

    proxy = getProxyIP().get("proxy")

    re = getRes(url, proxy)

    while re.status_code != 200:
        delProxyIP(proxy)
        proxy = getProxyIP().get("proxy")
        re = getRes(url, proxy)

    # print (re.status_code)

    # print (re.text)

    # print ("num of proxies : " + str(proxyNum))
    # print("proxy : { http : http://" + format(proxy) + "}")

    # 写入文件， 二进制写入
    cur_path = os.path.dirname(os.path.abspath(__file__))
    rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))
    down_path = os.path.join(rot_path, 'down')
    print(down_path)

    if not os.path.exists(down_path):
        try:
            os.mkdir(down_path)
        except FileExistsError:
            pass

    with open(down_path +"\\" + url_title, 'wb') as file:
        print(re.status_code)
        file.write(re.content)


def execDown(num):
    while num > 0:
        downFile()
        num -= 1
    # return num
