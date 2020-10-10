from selenium import webdriver
from lxml import etree
from selenium.webdriver import ActionChains
from time import sleep
import xdlj

# 打开网站
bro = webdriver.Chrome('chromedriver.exe')
url = 'https://www.bilibili.com/ranking/all/129/0/3'
bro.get(url=url)

# 获取源码
page_text = bro.page_source

# 解析源码并获取详情页网站
tree = etree.HTML(page_text)
url_list = tree.xpath(
    '//div[@class="rank-list-wrap"]//li//div[@class="info"]/a/@href')

for content_url in url_list[0:5]:
    bro.get(url=content_url)
    # 创建动作链
    share = bro.find_element_by_class_name('van-icon-videodetails_share')
    action = ActionChains(bro)
    action.click(share)
    bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(1)
    for i in range(5):
        action.move_by_offset(1, -10).perform()
        sleep(0.5)
    action.click()
