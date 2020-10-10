# -*- encoding:utf-8 -*-
'''
@文件        :练习正则爬图�?.py
@说明        :
@时间        :2020/07/14 11:34:10
@作�?        :韩淑�?
@软件        :VScode
'''

import requests
import re
import os
import xdlj


if __name__ == '__main__':
    if not os.path.exists('爬图'):
        os.mkdir("爬图")
    url = 'http://pic.netbian.com/'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
    page_text = requests.get(url=url, headers=headers).text
    ex = '<a href=".*?".*?<img src="(.*?)" alt.*?</b></a>'
    img_src_list = re.findall(ex, page_text, re.S)
    for src in img_src_list:
        src = 'http://pic.netbian.com' + src
        img_data = requests.get(url=src, headers=headers).content
        img_name = src.split('/')[-1]
        imgPath = '爬图/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img_data)
        print(img_name + '保存成功！！')
