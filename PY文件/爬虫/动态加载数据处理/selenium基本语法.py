from selenium import webdriver
from lxml import etree
from time import sleep
import os
import xdlj

# os检查是否存在并创建
if not os.path.exists('./化妆品'):
    os.mkdir('./化妆品')

# 实例化一个浏览器对象(传入浏览器的驱动程序)
bro = webdriver.Chrome(executable_path='chromedriver.exe')

# 让浏览器发起一个指定URL对应请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')

# 获取浏览器当前页面的页面源码数据
page_text = bro.page_source
tree = etree.HTML(page_text)
href_list = tree.xpath('//div[@id="FileItems"]/ul[@id="gzlist"]/li//a/@href')
name_list = tree.xpath('//div[@id="FileItems"]/ul[@id="gzlist"]/li/dl/@title')
# print(href_list)
# print(name_list)
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
    }
li_list = tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(5)
bro.quit()
