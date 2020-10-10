# -*- encoding:utf-8 -*-
"""
@文件        :bs4案例.py
@说明        :爬取三国演义小说所有的章节标题和章节内容
@时间        :2020/07/15 14:29:46
@作者        :韩淑熙
@软件        :VScode
"""

import requests
from bs4 import BeautifulSoup
import xdlj

if __name__ == "__main__":
    # 对首页的页面数据进行爬取
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).text
    # 在页面中解析出章节的标题和详情页URL
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    for li in li_list:
        title = li.a.text
        detail_url = 'http://www.shicimingju.com' + li.a['href']
        detail_text = requests.get(url=detail_url, headers=headers).text
        detail_soup = BeautifulSoup(detail_text, 'lxml')
        detail = detail_soup.find('div', class_="chapter_content").text
        fileName = '三国演义.txt'
        with open(fileName, 'a', encoding='utf-8') as fp:
            fp.write(title + '\n' + detail + '\n\n')
            print(title + '下载完成！！')
