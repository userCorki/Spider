import urllib.request               #������Ҫ�Ŀ�
import urllib.parse

def mySpider(url,addr):
    url = url       #Ҫʹ�õ���������
    headers={                           #��дHEADERͷ
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    parameters = {                      #�����ؼ���
        "wd":"�����Ǹ�����",
    }

    datas = urllib.parse.urlencode(parameters,encoding="utf-8")          #POST������Ҫ���˴���ΪBeyts����
    url = url+"/s?"+datas               #ƴ��URL

    requests = urllib.request.Request(url,method="GET")         #ʹ��GET�������󣬲���ҪDATA������POST������ҪDATA����
    resp = urllib.request.urlopen(requests)                     #�������������
    test = resp.read().decode()                                 #���룬��ʾ��ҳԴ����

    with open(addr,"w",encoding="utf8") as f:
        f.write(test)

mySpider(url="http://www.baidu.com",addr="C:/Users/IMNU_ADMIN/Desktop/�½��ı��ĵ� (2).txt")