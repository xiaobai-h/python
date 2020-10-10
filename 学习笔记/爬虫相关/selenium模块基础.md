## 展示

未见其人，先闻其声

<video src="https://5015060987.oss-cn-beijing.aliyuncs.com/video/selenium%E5%B1%95%E7%A4%BA.mp4"></video>

这逼格一下就上去了



![img](https://5015060987.oss-cn-beijing.aliyuncs.com/img/068B3DC1.gif)

## 基础

### selenium模块的基本使用

#### 问题： selenium模块和爬虫之间具有怎么样的关联？

- 便捷的获取网站中动态加载的数据
- 便捷实现模拟登录

#### 什么是selenium模块？

- 基于浏览器自动化的一个模块

#### ==selenium使用流程==

##### 环境安装：

```python
pip install selenium # 和其他库类似，这个selenium一定不能拼错
```

##### 下载浏览器驱动：

本人使用Chrome，所以贴出来ChromeDriver，其他浏览器请自行百度，大版本对即可，我的Chrome是85.0.4183.102，但使用85.0.4183.87可以正常使用

==下载路径==：http://chromedriver.storage.googleapis.com/index.html 

下载之后最好放到编写py程序的文件夹，便于后面引用

##### 实例化一个浏览器对象

```python
bro = webdriver.Chrome(executable_path='chromedriver.exe') #此处我放到同一文件夹下
```

![Chromedriver位置展示](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200911163442458.png)

##### 编写基于浏览器自动化的操作代码

- 发起请求：

```python
url = 'https://www.taobao.com/'
bro.get(url=url) # 此处以淘宝为例，虽然淘宝涉及到模拟登录
```

- 标签定位

```python 
serach_input = bro.find_element_by_id('q') # 此处find方法有很多
```

![定位搜索框](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200911163802865.png)

- 标签交互

```python
serach_input.send_keys('Python') # 此处你可以选择任意关键词
```

- 前进后退

```python
bro.back() # 看名字也知道是后退
bro.forward() # 前进
```

- 关闭浏览器

```python 
bro.quit()
```

### 全部代码

```python 
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

bro.get('https://www.baidu.com') # 此处又打开了一个网址

sleep(2)
# 回退
bro.back()

sleep(2)
# 前进
bro.forward()

sleep(5)
bro.quit()

```

## 写在最后

以后还会更新selenium，建议跟进(^_−)☆