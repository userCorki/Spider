import urllib.request               #������Ҫ�Ŀ�
import urllib.parse

def mySpider(url,addr):
    url = url                           #Ҫʹ�õ���������
    headers={                           #��дHEADERͷ
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    requests = urllib.request.Request(url,method="GET")         #ʹ��GET�������󣬲���ҪDATA������POST������ҪDATA����
    resp = urllib.request.urlopen(requests)                     #�������������
    test = resp.read().decode()                                 #���룬��ʾ��ҳԴ����

    with open(addr,"w",encoding="utf8") as f:
        f.write(test)

mySpider(url="http://www.17k.com/chapter/2933095/36699279.html",addr="C:/Users/IMNU_ADMIN/Desktop/�½��ı��ĵ� (4).txt")