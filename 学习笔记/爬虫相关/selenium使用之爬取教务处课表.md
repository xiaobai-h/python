## 未见其人，先闻其声

<video src="https://5015060987.oss-cn-beijing.aliyuncs.com/video/Rec%200001.mp4"></video>

==正如上述，点击运行之后，全部自动化处理，这逼格一下就上去了==

## 代码实现

### 一.准备工作

#### 	1.下载驱动

本人使用Chrome，所以贴出来ChromeDriver，其他浏览器请自行百度，大版本对即可，我的Chrome是85.0.4183.102，但使用85.0.4183.87可以正常使用

==下载路径==：http://chromedriver.storage.googleapis.com/index.html 

#### 	2.环境安装

```python 
pip install selenium # 和其他库类似，这个selenium一定不能拼错
```



### 二.导入模块

首先你当然得导入webdriver，etree和xlwt三个模块。分别对应自动化处理浏览器登录和点击、xpath分析网页元素和持久化存储。

```python 
from selenium import webdriver
from lxml import etree
from time import sleep  # 时间暂停
import xlwt
```

### 三.自动化登录

#### 1.实例化浏览器对象

```python 
bro = webdriver.Chrome('executable_path='./chromedriver.exe)
```

#### 2.指定url进行访问

```python
url = 'https://jwcnew.webvpn.nefu.edu.cn/dblydx_jsxsd/'
bro.get(url=url)
```

![如图所示](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912070651359.png)



#### 3.获取账号和密码标签并登录(通过selenium)

![账号标签](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912070835207.png)

![密码标签](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912071116750.png)

![登录标签](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912073534611.png)

可见它账号id标签为un(可以使用其他标签定位)

密码标签为pd

登录按钮的class标签为login_box_landing_btn

```python 
account_input = bro.find_element_by_id('un')  # 定位账号
password_input = bro.find_element_by_id('pd')  # 定位密码
account_input = bro.send_keys('2019214286')  # 输入账号
password_input = bro.send_keys('xxxxxxxx') # 输入密码
login = bro.find_element_by_class_name('login_box_landing_btn')  # 定位登录
login.click()  # 字如其意，点击登录按钮
```

登陆完之后，他会转到另一个登录界面

![另一个登录界面](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912073901365.png)

此时再次使用上面用到的定位然后输入就不在啰嗦

```python
account_input_two = bro.find_element_by_name('USERNAME')  # 定位账号
password_input_two = bro.find_element_by_name('PASSWORD')  # 定位密码

account_input_two.send_keys('2019214286')  # 输入账号
password_input_two.send_keys('xxxx')  # 输入密码吗

login_three = bro.find_element_by_id('btnSubmit')  # 定位登录按钮
login_three.click()  # 登录到教务管理系统个人界面
```

![个人界面](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912074354006.png)



#### 4.获取课程表界面

观看上图，可见**我的课表**就在第三排第一个

通过标签定位，然后click即可

```python 
login_four = bro.find_element_by_class_name('block7')  
login_four.click()  # 进入课程表界面
```

![课程表界面](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912074816651.png)





### 四.解析课程表界面(通过xpath)

#### 1.获取页面源码

```python
page_text = bro.page_source  # 获取页面源码
tree = etree.HTML(page_text)  # 创建一个etree对象
```

#### 2.获取具体内容

![分析element](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912075254151.png)

看上图，感觉挺简单的，都在tbody标签下，也涉及不到iframe。**开整！！**

##### 	1.第一行

第一行星期还算简单，都在相同标签下，见图

![第一行](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912075556411.png)

```python
first_line_list = tree.xpath('//tbody/tr[1]/th/text()')  # 获取第一行
```

##### 2.第一列

原本我想着，他会把下面所有内容都放到一个标签下，直接解析：~~//tbody/tr/div/text()~~， 查看源码才发现，他是把第一列都放在th标签下，而具体课表都在div标签下，直接见图：

![第一列和内容的区别](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912080212469.png)

所以第一列也是需要单独解析出来

~~又因为第一列的元素都不在一个标签下，所以需要一个range循环~~

```python
first_row_list = []  # 创建一个空列表
for i in range(7):
    first_row_list.append(tree.xpath('//tbody/tr[i+2]/th/text()')[0])
```

***如果真的这么写的话，就会出现下面这种情况***

![image-20200912081601382](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912081601382.png)

我也不知道为什么tr标签不能带入未知量

![tr标签不能用未知量](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912081830294.png)



==所以正确获取第一列的方法是==  ~~虽然有点笨，但结果是对的~~

```python
first_row_list = []
first_row_list.append(tree.xpath('//tbody/tr[2]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[3]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[4]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[5]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[6]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[7]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[8]/th/text()')[0])
```

##### 3.课表具体内容

```python
content_list = tree.xpath('//tbody/tr/td/div[2]/text()')
```

其实在爬取具体课表的时候，发现了一个好玩的

![div与div的区别](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912082302652.png)

虽然我不懂前端，但看这也是可以知道编写课表的时候第一次没考虑到老师，然后又写了一个div，这也是为什么我上面写div[2]

![img](https://5015060987.oss-cn-beijing.aliyuncs.com/img/017C0017.gif)

到此为止所有课表相关的数据爬取下来了，下一步就是保存了

### 五.持久化存储

如果用的是flake8，就会发现上面有一个会一直报错，

**'xlwt' imported but unused**

```python
import xlwt  # 这是因为下面还没用到
```

#### 1.创建Workbook

```python 
book = xlwt.Workbook(encoding='unicode')  # 第一次我用的是utf-8,会报错，就换了
sheet = book.add_sheet(u'课程表', cell_overwrite_ok=True)
```

#### 2.保存课表

和上面对应，分别保存第一行，第一列和课表具体内容

```python
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
```

#### 3.储存位置

```python
book.save('./课程表.xls')  # 我直接在本目录下保存，第一次用xlsx报错，就换成xls...
```

### 关闭selenium

```python
sleep(4)  # 让浏览器暂停一下
bro.quit()  # 退出模拟浏览器
```

到此便完成全部工作，展示一下结果

![课程表](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200912083634120.png)



## 程序代码

```python
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
password_input.send_keys('xxxxxxxx')

# 点击立即到教务处登录
login = bro.find_element_by_class_name('login_box_landing_btn')
login.click()

account_input_two = bro.find_element_by_name('USERNAME')
password_input_two = bro.find_element_by_name('PASSWORD')

account_input_two.send_keys('2019214286')
password_input_two.send_keys('xxxxxxxxx')

login_three = bro.find_element_by_id('btnSubmit')
login_three.click()  # 登录教务处

login_four = bro.find_element_by_class_name('block7')  # 进入课程表界面
login_four.click()


# 2.解析课程表界面，并保存到本地
page_text = bro.page_source
tree = etree.HTML(page_text)
first_line_list = tree.xpath('//tbody/tr[1]/th/text()')  # 获取第一行星期内容
first_row_list = []
first_row_list.append(tree.xpath('//tbody/tr[2]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[3]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[4]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[5]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[6]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[7]/th/text()')[0])
first_row_list.append(tree.xpath('//tbody/tr[8]/th/text()')[0])  # 获取第一列节数内容
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

```



## 总结

### 1. selenium无敌，selenium无敌，selenium无敌

### 2.爬取第一列的时候还有一点问题没解决，不能循环

### 3. Python处理Excel表格是现学现卖的，没有处理好单元格大小问题

### 4.如果你也认为这篇文章有趣，请一定要评论，转发并投币



![img](https://5015060987.oss-cn-beijing.aliyuncs.com/img/018AE10C.gif)