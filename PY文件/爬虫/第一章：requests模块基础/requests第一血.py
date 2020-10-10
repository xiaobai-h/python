# -*- encoding: utf-8 -*-
"""
@文件        :requests第一血.py
@说明        :
@时间        :2020/07/07 12:58:15
@作者        :韩淑熙
@软件        :PyCharm
"""

import requests

# 需求：爬去搜狗首页的页面数据
if __name__ == "__main__":
    # 1.指定URL
    url = "https://www.qq.com/"
    # 2.发起请求
    # get方法会返回一个响应对象
    response = requests.get(url)
    # 3.获取响应数据.text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # 4.持久化存储
    with open(r'D:\python_vscode\PY文件\爬虫\qq.html', 'w',
              encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束！！！")
