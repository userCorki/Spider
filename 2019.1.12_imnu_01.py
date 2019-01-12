import urllib.request               #导入需要的库
import urllib.parse

def mySpider(url,addr):
    url = url       #要使用的搜索引擎
    headers={                           #改写HEADER头
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    parameters = {                      #搜索关键字
        "wd":"胡旺是个好人",
    }

    datas = urllib.parse.urlencode(parameters,encoding="utf-8")          #POST请求需要将此处改为Beyts类型
    url = url+"/s?"+datas               #拼接URL

    requests = urllib.request.Request(url,method="GET")         #使用GET方法请求，不需要DATA参数；POST请求需要DATA参数
    resp = urllib.request.urlopen(requests)                     #发送浏览器请求
    test = resp.read().decode()                                 #解码，显示网页源代码

    with open(addr,"w",encoding="utf8") as f:
        f.write(test)

mySpider(url="http://www.baidu.com",addr="C:/Users/IMNU_ADMIN/Desktop/新建文本文档 (2).txt")