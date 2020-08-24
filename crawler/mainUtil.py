import requests
from lxml import etree


# @ param headers 浏览器的headers
# @ param aim_url 目标url

def main(headers, aim_url):
    r = requests.get(aim_url, headers=headers)

    #print(r.text)

    s = etree.HTML(r.text)

    #获取问题内容
    rst_content = s.xpath('//*[@class="QuestionHeader-title"]/text()')[0]

    #获取问题描述
    rst_describe = s.xpath('//*[@class="RichText ztext"]/text()')[0]

    #获取关注量和浏览量
    rst_number = s.xpath('//*[@class="NumberBoard-itemValue"]/text()')
    concern_num = rst_number[0]
    browing_num = rst_number[1]

    #输出
    print('问题：', rst_content, '\n'
          , '描述：', rst_describe, '\n'
          , '关注数：', concern_num, '\n'
          , '浏览量：', browing_num)


