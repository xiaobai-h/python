
import requests
import json
from rich import print
httpUrl = "https://apifang.58.com/aurora/query_list?callback=jQuery112406972431253543614_1599485866838&client=0&region=right&page=1&version=201610&pageSize=10&cityId=497&cateId=12&userId=&cookie=&pageType=esf&areaId=497&shangquanId=&_=1599485866839"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
response = requests.get(url = httpUrl, headers = headers).content.decode()
string = response.replace("jQuery112406972431253543614_1599485866838(", "")[0:-1:1]
houseList = json.loads(string)['data']['houseList']

# print(json.loads(string)['data']['houseList'])
for i in houseList:
    print(i['xiaoquName'])
    # print(i['houseName'])
    print(i['url'])
    print(i['areaName'])
    print(i['price'])
    print(i['shangquanName'])
