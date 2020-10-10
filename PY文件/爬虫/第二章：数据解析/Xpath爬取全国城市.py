import requests
from lxml import etree
import xdlj

if __name__ == "__main__":
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    city_list = tree.xpath('//div[@class="all"]/div[@class="bottom"]/ul[@class="unstyled"]//li/a/text()')
    a = 1
    for city in city_list:
        with open('AllCities.txt', 'a+', encoding='utf-8') as fp:
            fp.write(str(a) + ' : ' + city + '\n')
            a = a + 1
            print(city + '保存成功')
