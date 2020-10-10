from selenium import webdriver
from time import sleep
import xdlj

# 实例化一个driver对象
bro = webdriver.Chrome(executable_path='chromedriver.exe')

# 指定URL
url = 'https://www.taobao.com/'
bro.get(url=url)

# 定位标签
serach_input = bro.find_element_by_id('q')

# 标签交互
serach_input.send_keys('iphone')

# 执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')

sleep(2)
# 点击搜索
btn = bro.find_element_by_class_name('btn-search')
btn.click()

bro.get('https://www.baidu.com')

sleep(2)
# 回退
bro.back()

sleep(2)
# 前进
bro.forward()

sleep(5)
bro.quit()
