# -*- encoding: utf-8 -*-
'''
@文件        :requests实战之肯德基餐厅查询.py
@说明        :当一个地点肯德基店铺数量不超过100个时，全部显示
@时间        :2020/07/09 15:02:30
@作者        :韩淑熙
@软件        :VScode
'''


import requests
import xdlj


if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58'
    }
    kw = input("input a city keyword")
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '100',
    }
    response = requests.post(url=url, headers=headers, data=data)
    page_text = response.text
    fileName = kw + '.json'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print("over!!")
