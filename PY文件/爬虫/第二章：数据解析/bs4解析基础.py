# -*- encoding:utf-8 -*-
'''
@文件        :bs4解析基础.py
@说明        :
@时间        :2020/07/15 13:09:57
@作者        :韩淑熙
@软件        :VScode
'''

from bs4 import BeautifulSoup
import xdlj

if __name__ == "__main__":
    # 将本地的HTML文档中的数据加载到该对象中
    fp = open('test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # print(soup.a)  # soup.tagName 返回的是HTML中第一次出现的tagNanme
    # print(soup.div)
    # print(soup.find('div'))  # print(soup.div)
    print(soup.find('div', class_='song').get_text())
    # print(soup.find_all('a'))
    # print(soup.select('.tang'))  # 返回的列表
    # print(soup.select('.tang > ul a')[0]['href'])
