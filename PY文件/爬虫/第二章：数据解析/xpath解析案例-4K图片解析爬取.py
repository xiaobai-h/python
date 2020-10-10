import requests
from lxml import etree
import os
import xdlj  # 解决相对路径问题

if __name__ == "__main__":

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    for i in range(1, 2):
        url = 'http://pic.netbian.com/4kmeinv/'
        url = url + 'index_' + str(i) + '.html'
        # print(url)
        response = requests.get(url=url, headers=headers)
        # response.encoding = 'utf-8'
        page_text = response.text

        # 数据解析： src的属性值，alt属性
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]//li')

        # 创建一个文件夹
        # if not os.path.exitsts("./爬图"):
        #     os.mkdir("./爬图")

        for li in li_list:
            img_src = 'http://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            # print(img_name, img_src)
            img_data = requests.get(url=img_src, headers=headers).content
            img_Path = '爬图/' + img_name
            with open(img_Path, 'wb') as fp:
                fp.write(img_data)
                print(img_name + '保存成功！')
