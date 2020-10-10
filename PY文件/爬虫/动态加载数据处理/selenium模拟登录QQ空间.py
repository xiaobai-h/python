from selenium import webdriver
from lxml import etree
from time import sleep
import xdlj

bro = webdriver.Chrome('chromedriver.exe')
url = 'https://qzone.qq.com/'
bro.get(url=url)

bro.switch_to.frame('login_frame')
link = bro.find_element_by_id('switcher_plogin')
link.click()

account_input = bro.find_element_by_id('u')
password_input = bro.find_element_by_id('p')

account_input.send_keys('501560987')
password_input.send_keys('Hsx0108..')

button = bro.find_element_by_class_name('btn')
button.click()

img = bro.find_element_by_class_name('tc-jpp-img unselectable')
