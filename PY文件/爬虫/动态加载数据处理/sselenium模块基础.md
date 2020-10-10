selenium模块的基本使用

问题： selenium模块和爬虫之间具有怎么样的关联？
        - 便捷的获取网站中动态加载的数据
        - 便捷实现模拟登录
什么是selenium模块？
    - 基于浏览器自动化的一个模块
    
selenium使用流程：
    - 环境安装
        这个和其他库类似： pip install selenium  //selenium一定不能拼错
    - 下载浏览器驱动(本人使用Chrome，所以贴出来Chromedriver，其他浏览器请自行百度，大版本对即可，我的Chrome是85.0.4183.102，但使用85.0.4183.87可以正常使用)
            下载路径： http://chromedriver.storage.googleapis.com/index.html   
    - 实例化一个浏览器对象
    - 编写基于浏览器自动化的操作代码
        - 发起请求： get(url)
        - 标签定位： find()系列的方法
        - 标签交互： send_keys('xxx')
        - 执行js程序： excute_script('jsCode')
        - 前进，后退： back(), forward()
        - 关闭浏览器： quit()

    - selenium处理iframe
        - 如果定位的标签存在与iframe标签之中，则必须使用switch_to_frame(id)
        - 动作链(拖动) ：from selenium.webdriver import ActionChains
            - 实例化一个动作链对象：action = ActionChains(bro)
            - click_and_hold(div) ： 长按且点击操作
            - move_by_offset(x,y)
            - perform()让动作链立即执行
            - action.release()释放动作链对象