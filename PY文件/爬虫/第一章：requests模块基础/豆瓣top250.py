# -*- encoding:utf-8 -*-
'''
@文件        :豆瓣top250.py
@说明        :
@时间        :2020/07/13 12:53:27
@作者        :韩淑熙
@软件        :VScode
'''

import requests
import xdlj


if __name__ == "__main__":
    urls = ['https://movie.douban.com/top250?start='+str(n)+'&filter=' for n in range(0, 250, 25)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    fileName = '豆瓣top250.json'
    for url in urls:
        page_text = requests.get(url=url, headers=headers).text
        with open(fileName, 'a', encoding='utf-8') as fp:
            fp.write(page_text)
    print('over!!')
