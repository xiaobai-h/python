import requests
from lxml import etree
import os
import xdlj

if __name__ == "__main__":
    if not os.path.exists('./模板'):
        os.mkdir('./模板')

    for i in range(1, 2):
        url = 'http://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&issale=&classID=864&page=' + str(i)
        headers = {
            'User-Agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61"
        }
        page_text = requests.get(url=url, headers=headers).text
        tree = etree.HTML(page_text)
        href_list = tree.xpath('//div[@class="sc_warp  mt20"]/div/div/div/a/@href')
        alt_list = tree.xpath('//div[@class="sc_warp  mt20"]/div//div/a/img/@alt')
        for href, alt in zip(href_list, alt_list):
            down_text = requests.get(url=href, headers=headers).text
            down_tree = etree.HTML(down_text)
            down_url = down_tree.xpath('//div[@class="clearfix mt20 downlist"]//li[4]/a/@href')[0]
            down_data = requests.get(url=down_url, headers=headers).content
            down_name = alt
            FileName = '模板/' + alt + '.rar'
            with open(FileName, 'wb') as fp:
                fp.write(down_data)
                print(down_name + '下载成功！！')
