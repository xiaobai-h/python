import requests
import xdlj
# from lxml import etree

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
