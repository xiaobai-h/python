# -*- encoding: utf-8 -*-
'''
@文件        :requests实战之药监总局相关数据爬取.py
@说明        :
@时间        :2020/07/10 08:32:50
@作者        :韩淑熙
@软件        :VScode
'''
import requests
import xdlj
import json

if __name__ == "__main__":
    # 批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # UA伪装
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58'
    }
    # 参数的封装
    id_list = []  # 存储企业的id值
    all_data_list = []  # 存储企业详情页
    for page in range(1, 2):
        page = str(page)
        data = {
            'on': 'true',
            'page': '1',
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    de_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data_id = {
            'id': id
        }
        dic_obj = requests.post(url=de_url, headers=headers, data=data_id).json()
        all_data_list.append(dic_obj)
    fp = open('药监总局.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print("over!!")
