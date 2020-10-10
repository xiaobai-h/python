# -*- encoding: utf-8 -*-
'''
@文件        :requests实战之豆瓣电影爬取.py
@说明        :
@时间        :2020/07/09 14:18:22
@作者        :韩淑熙
@软件        :VScode
'''


import requests
import xdlj
import json
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  # 从库中第几部电影去取
        'limit': '20',  # 一次请求取出的个数
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
    response = requests.get(url=url, params=params, headers=headers)

    list_data = response.json()
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print("over!!")
