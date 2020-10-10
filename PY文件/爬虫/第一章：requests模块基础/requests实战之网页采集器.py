# -*- encoding: utf-8 -*-
'''
@文件        :requests实战之网页采集器.py
@说明        :
@时间        :2020/07/07 13:26:22
@作者        :韩淑熙
@软件        :VScode
'''


# UA检测：门户网站的服务器会检测对应请求的载体身份标识，浏览器则为正常请求
# UA： User_Agent(请求载体的身份标识)

# UA伪装
import requests
import xdlj
if __name__ == "__main__":
    # UA伪装：将对应的User_Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58'
    }
    url = 'https://www.sogou.com/web'
    # 处理URL携带的参数： 封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }

    # 对指定的URL发起的请求是携带参数的，并且已处理参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！！')
