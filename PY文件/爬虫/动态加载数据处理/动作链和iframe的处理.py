from selenium import webdriver
# 导入动作链类
from selenium.webdriver import ActionChains
import xdlj
from time import sleep

bro = webdriver.Chrome('chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 如果定位的标签是存在于ifranme标签之中的则必须通过如下操作再进行标签定位
bro.switch_to.frame('iframeResult')  # 切换浏览器标签定位的作用域

div = bro.find_element_by_id('draggable')

# 动作链
action = ActionChains(bro)
# 点击并长按
action.click_and_hold(div)

for i in range(5):
    # perform()立即执行动作链操作
    # move_by_offset(x,y) : x水平， y竖直
    action.move_by_offset(17, 0).perform()
    sleep(0.3)

# 释放动作链
action.release()
bro.quit()
