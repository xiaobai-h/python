# -*- encoding: utf-8 -*-
'''
@File    :   验证码破解.py
@Time    :   2020/09/10 10:49:21
@Author  :   Hans
@Version :   1.0
@Contact :   501560987@qq.com
'''

import requests
from lxml import etree
import xdlj


if __name__ == "__main__":
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    img_url = 'https://so.gushiwen.cn/' + tree.xpath('//div[@class="mainreg2"]/div[4]/img/@src')[0]
    img_data = requests.get(url=img_url, headers=headers).content
    fileName = '验证码.jpg'
    with open(fileName, 'wb') as fp:
        fp.write(img_data)
        print(fileName + '下载成功！！')
