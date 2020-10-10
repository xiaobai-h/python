from selenium import webdriver
from lxml import etree
from time import sleep
import xlwt
import xdlj


# 1.实现从登录到课程表界面开始
bro = webdriver.Chrome(executable_path='chromedriver.exe')

url = 'https://jwcnew.webvpn.nefu.edu.cn/dblydx_jsxsd/'
bro.get(url=url)

# 获取登录账号和密码的位置
account_input = bro.find_element_by_id('un')
password_input = bro.find_element_by_id('pd')

# 输入账号密码
account_input.send_keys('2019214286')
# 密码就不漏出来了


password_input.send_keys('Hsx501560987')

# 点击立即到教务处登录
login = bro.find_element_by_class_name('login_box_landing_btn')
login.click()

account_input_two = bro.find_element_by_name('USERNAME')
password_input_two = bro.find_element_by_name('PASSWORD')

account_input_two.send_keys('2019214286')
password_input_two.send_keys('Hsx501560987')

login_three = bro.find_element_by_id('btnSubmit')
login_three.click()  # 登录教务处

# 临时添加，因为原来没有选择导师，现在添加了一个选择导师，不点击进不去
# bro.switch_to.alert.accept()

login_four = bro.find_element_by_class_name('block7')  # 进入课程表界面
login_four.click()


# 2.解析课程表界面，并保存到本地
page_text = bro.page_source
tree = etree.HTML(page_text)
first_line_list = tree.xpath('//tbody/tr[1]/th/text()')  # 获取第一行星期内容
first_row_list = [tree.xpath('//tbody/tr[2]/th/text()')[0], tree.xpath('//tbody/tr[3]/th/text()')[0],
                  tree.xpath('//tbody/tr[4]/th/text()')[0], tree.xpath('//tbody/tr[5]/th/text()')[0],
                  tree.xpath('//tbody/tr[6]/th/text()')[0], tree.xpath('//tbody/tr[7]/th/text()')[0],
                  tree.xpath('//tbody/tr[8]/th/text()')[0]]
content_list = tree.xpath('//tbody/tr/td/div[2]/text()')  # 获取课表具体内容
book = xlwt.Workbook(encoding='unicode')  # 创建Workbook，相当于创建Excel
sheet = book.add_sheet(u'课程表', cell_overwrite_ok=True)
for i in range(8):
    sheet.write(0, i, first_line_list[i])  # 保存第一行
for j in range(7):
    sheet.write(j+1, 0, first_row_list[j])  # 保存第一列
for i in range(7):
    sheet.write(1, i+1, content_list[i])
    sheet.write(2, i+1, content_list[7+i])
    sheet.write(3, i+1, content_list[14 + i])
    sheet.write(4, i+1, content_list[21+i])
    sheet.write(5, i+1, content_list[28+i])
    sheet.write(6, i+1, content_list[35+i])
book.save('./课程表.xls')
sleep(4)
bro.quit()
