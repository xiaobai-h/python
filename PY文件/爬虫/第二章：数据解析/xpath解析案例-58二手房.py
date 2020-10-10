# -*- encoding:utf-8 -*-
'''
@文件        :xpath解析案例-58二手房.py
@说明        :爬取58二手房中的房源信息
@时间        :2020/07/18 15:21:18
@作者        :韩淑熙
@软件        :VScode
'''


import requests
from lxml import etree
import xdlj

if __name__ == '__main__':
    url = 'https://bj.58.com/ershoufang/?PGTID=0d100000-001f-1904-0bdf-441640371698&ClickID=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    name_list = tree.xpath('//ul[@class="house-list-wrap"]//div[@class="list-info"]/h2[@class="title"]/a/text()')
    price_list = tree.xpath('//ul[@class="house-list-wrap"]//div[@class="price"]/p[@class="sum"]/b/text()')
    fp = open('58北京二手房(时更).txt', 'w', encoding='utf-8')
    for name, price in zip(name_list, price_list):
        fp.write(name + '的价格为' + price + '万\n')
        print(name + '保存成功！')
