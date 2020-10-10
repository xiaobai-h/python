# -*- encoding: utf-8 -*-
"""
@File       : 1. 同步爬虫.py
@Time       : 2020/10/9 19:02
@Author     : Hans
@Software   : PyCharm
"""

import requests
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61"
}
urls = {
    'http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar',
    'http://zjlt.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10229.rar',
    'http://xmdx.sc.chinaz.net/Files/DownLoad/JIANLI/201904/jianli02231.rar'
}


def get_content(url):
    # get方法是一个阻塞的方法
    reponse = requests.get(url=url, headers=headers)
    if reponse.status_code == 200:
        return reponse.content


def parse_content(content):
    print("相应数据长度为", len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)
