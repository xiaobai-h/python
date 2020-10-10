# -*- encoding: utf-8 -*-
'''
@文件        :requests实战之破解百度翻译.py
@说明        :
@时间        :2020/07/09 09:17:37
@作者        :韩淑熙
@软件        :VScode
'''


import requests
import xdlj
import json

if __name__ == "__main__":
    # 1.指定URL
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
    kw = input('Please input what you want to translate:')
    # 3.post请求参数处理（同get请求一致）
    data = {
        'kw': kw
    }
    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取响应数据: json()方法返回的是obj(若果确认响应数据是json类型的，才可以使用json())
    dic_obj = response.json()
    # 6.持久化存储
    fileName = kw + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print('over!!!')
