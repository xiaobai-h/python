### 确定目标

​	先上今日目标网站：https://ss.netnr.com/wallpaper#6，顺便贴张图，自行理解。



![古风  古装  红衣  美女  妖娆](https://5015060987.oss-cn-beijing.aliyuncs.com/img/t01606e77accd306176.jpg)



### 爬虫过程

思维固化，以前爬虫，总是**Ctrl + Shift + i** 然后 **Ctrl + Shift + c**， 直接在页面中选择一个元素进行检查，

![image-20200909202830951](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200909202830951.png)

想着挺简单的，谁知到后面一直显示找不到，一度让我怀疑自己Xpath路径找错，然后等我查看网站源代码，

![image-20200909203503228](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200909203503228.png)

简单的一批，根本就没有图片链接，我才料到这网站为了防止爬虫大量下载图片，隐藏了真正储存图片链接的域名。~~哎，道行太浅啊~~ ，于是，我就打开network，向下滑，获得了一个XHR请求，

![image-20200909204015342](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200909204015342.png)

复制了一下响应对象，看到是字典型，于是我就直接

```java
img_list = page_text('data')
```

得到结果为

```java
string indices must be integers
```

百度了一下好像是json格式导致

第一个我想到直接

```java 
page_text = requests.get(url=url, headers=headers).json //基础知识也忘了，ε=(´ο｀*)))唉
```



然后通过百度得知json()，就是下面才是对的

```java
page_text = requests.get(url=url, headers=headers).json()
```

顺便再复习一下三者关系：

- response.text : 返回一个字符串\n
- content : 返回二进制\n
- json() : 返回对象

### 爬虫源码

```java
import requests
import xdlj //没错，就是相对路径，VScode特色，ennnnn

if __name__ == "__main__":
    url = 'https://bird.ioliu.cn/v2?url=http%3A%2F%2Fwallpaper.apc.360.cn%2Findex.php%3Fc%3DWallPaper%26start%3D1%26count%3D12%26from%3D360chrome%26a%3DgetAppsByCategory%26cid%3D6'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).json()
    img_list = page_text['data']
    for img in img_list:
        img_url = img['url']
        img_name = img['utag']
        img_data = requests.get(url=img_url, headers=headers).content
        img_Path = '爬图/' + img_name + '.jpg'
        with open(img_Path, 'wb') as fp:
            fp.write(img_data)
            print(img_name + '保存成功！！！')

```



### 爬虫成果

顺便贴几张爬取的自我感觉还阔以的



![古风  古装  红衣  美女  妖娆](https://5015060987.oss-cn-beijing.aliyuncs.com/img/%E5%8F%A4%E9%A3%8E%20%20%E5%8F%A4%E8%A3%85%20%20%E7%BA%A2%E8%A1%A3%20%20%E7%BE%8E%E5%A5%B3%20%20%E5%A6%96%E5%A8%86.jpg)



![清纯 水管 清凉 夏天](https://5015060987.oss-cn-beijing.aliyuncs.com/img/t01493a30ef5285f801.jpg)



![党妹cosplay  异域风情](https://5015060987.oss-cn-beijing.aliyuncs.com/img/t0180847dcd4fe8913c.jpg)



![古风](https://5015060987.oss-cn-beijing.aliyuncs.com/img/t0186075092ae205f7d.jpg)

