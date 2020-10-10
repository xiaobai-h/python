# -*- encoding:utf-8 -*-
'''
@文件        :正则解析.py
@说明        :爬取糗事百科中糗图板块下所有的糗图图片
@时间        :2020/07/13 14:28:02
@作者        :韩淑熙
@软件        :VScode
'''

import requests
import re
import xdlj
# import os

if __name__ == '__main__':
    # 创建一个文件夹，保存所有图片
    # if not os.path.exists('qiutuLibs'):
    #     os.mkdir('qiuquLibs')
    urls = ['https://www.qiushibaike.com/imgrank/page/' + str(n) + '/' for n in range(1, 14)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    # 使用通用爬虫对URL对应的一整张页面进行爬取
    for url in urls:
        page_text = requests.get(url=url, headers=headers).text
        # 使用聚焦爬虫将页面中所有图片
        img_src_list = re.findall(ex, page_text, re.S)  # re.S单行匹配， re.M多行匹配
        for src in img_src_list:
            # 拼接出一个完整的图片URL
            src = 'https:' + src
            # 请求到了图片的二进制数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            # 图片存储的路径
            imgPath = 'qiuquLibs/' + img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功！！')
