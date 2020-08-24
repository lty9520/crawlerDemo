import requests
import urllib.request

def changeIP():
    # 查询IP http://ip.chinaz.com/getip.aspx
    url = 'http://ip.chinaz.com/getip.aspx'

    print('origin IP : ' + requests.get(url).text)

    # 构建一个代理IP的格式
    # IP
    ip_data = "47.94.230.42"
    # 端口
    port_data = "9999"
    # 固定IP格式
    new_data = {
        "http": ip_data + ":" + port_data
    }

    # proxies = IP requests模块构建请求
    print("after proxy IP : " + requests.get(url, proxies=new_data).text)

    # 切回自己的IP 当 当前IP失效后向代理IP提供商获取新IP时需要自己的ip
    print("change back me IP : " + requests.get(url, proxies={"http": ""}).text)

