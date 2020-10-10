# -*- encoding:utf-8 -*-
'''
@文件        :xpath解析基础.py
@说明        :
@时间        :2020/07/18 13:50:53
@作者        :韩淑熙
@软件        :VScode
'''

from lxml import etree
import xdlj

if __name__ == '__main__':
    # 已实例化一个etree对象，并且将被解析的源码加载到了该对象中
    tree = etree.parse('test.html')
    # r = tree.xpath('/html/body/div')
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div[@class="song"]/p[3]')
    # r = tree.xpath('//div[@class="song"]/p')
    # r = tree.xpath('//div[@class="tang"]//li[7]/i/text()')[0]
    # r = tree.xpath('//li[7]//text()')
    r = tree.xpath('//div[@class="tang"]//text()')
    r = tree.xpath('//div[@class="song"]/img/@src')[0]
    print(r)
