# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     getFile.py
   Description :   down file from url
   Author :       LHY
   date：          2020/08/19
-------------------------------------------------
   Change Activity:
                   2020/08/19: getFile
-------------------------------------------------
"""
__author__ = 'LHY'

import requests


#随机获取一个ip
def getProxyIP():
    return requests.get("http://127.0.0.1:5000/get/").json()


#删除不可用IP
#@param proxy 不可用ip
def delProxyIP(proxy):
    requests.get("http://127.0.0.1:5000/delete/?proxy={}".format(proxy))

#获取数据库中的ip总数(bytes格式）
#eval（bytes) 转换成字典['count'] 取值
def getProxyNum():
    return eval(requests.get("http://127.0.0.1:5000/get_status/").content)['count']


def downFile():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

    # cookies KV style
    cookies = {
        "_ga": "GA1.2.674636311.1596542605",
        "cirgu": "_1_lQW3CauilVNWfPtDsrnQ542KhXCaSTVRqjirTFiMwrSIKx3U0HMoVeEVHNcJf1uohw%3D%3D",
        "_gid": "GA1.2.859316147.1598277611"
    }

    url = 'https://www.researchgate.net/publication/335405853_AN_AUTOMATIC_EXTRACTION_METHOD_FOR_THE_PARAMETERS_OF_MULTI-LOD_BIM_MODELS_FOR_TYPICAL_COMPONENTS_OF_WOODEN_ARCHITECTURAL_HERITAGE/fulltext/5d6483b4299bf1f70b0eb45c/AN-AUTOMATIC-EXTRACTION-METHOD-FOR-THE-PARAMETERS-OF-MULTI-LOD-BIM-MODELS-FOR-TYPICAL-COMPONENTS-OF-WOODEN-ARCHITECTURAL-HERITAGE.pdf?_sg%5B0%5D=c8N4liVTvgrC3wnXbl-OvCotvOBNotwIBNqzcOCaVvZGyWSPg2M1Lvgz0-tB8d1hEgo4s1yYFknhqlBxTfzvTw.W808eGgryZqEUSDODjIK9aK_W9z_Jrw36KoXv3kNZx3XoUC6S7YSYpQ1U2uIbGPCPjcaiXu3UMeOweFropj9fw&_sg%5B1%5D=RR_QIxcvQq1TKyayg5wNIH_J5t9raNYhx8vAAnvxvGkp_9fkK05A_aSh4cBWUOy_7jzsZlYCgpFVAAiW4rhxs0fiLxZi_2ZNMMQ0V-dOLDLW.W808eGgryZqEUSDODjIK9aK_W9z_Jrw36KoXv3kNZx3XoUC6S7YSYpQ1U2uIbGPCPjcaiXu3UMeOweFropj9fw&_iepl='


    proxy = getProxyIP().get("proxy")
    proxyNum = getProxyNum()
    # 发起请求，获取二进制数据
    re = requests.get(url, headers=headers
                            , cookies=cookies
                            , proxies={"http": "http://{}".format(proxy)})

    #print (re.status_code)

    #print (re.text)

    print ("num of proxies : " + str(proxyNum))
    print("proxy : { http : http://" + format(proxy) + "}")

    # 写入文件， 二进制写入
    with open('test.pdf', 'wb')  as file:
        file.write(re.content)

