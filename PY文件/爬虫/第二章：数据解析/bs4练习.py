# -*- encoding:utf-8 -*-
'''
@文件        :bs4练习.py
@说明        :
@时间        :2020/07/18 09:59:05
@作者        :韩淑熙
@软件        :VScode
'''


import requests
from bs4 import BeautifulSoup
import xdlj

if __name__ == '__main__':
    url = 'http://www.shicimingju.com/book/shiji.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
    page_text = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li > a')
    print(li_list)
    for li in li_list:
        detail_url = 'http://www.shicimingju.com' + li['href']
        title = li.text
        detail_text = requests.get(url=detail_url, headers=headers).text
        detail_soup = BeautifulSoup(detail_text, 'lxml')
        detail = detail_soup.find('div', class_='chapter_content').text
        fileName = '史记.txt'
        with open(fileName, 'a', encoding='utf-8') as fp:
            fp.write(title + '  ' + detail + '\n\n')
            print(title + '爬取成功！！')
