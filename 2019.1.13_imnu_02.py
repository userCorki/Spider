import requests

response = requests.get("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808")

aimText_addr = response.text.split("\r\n")

for url in aimText_addr:
    print("���ڷ��ʵ�ַ��" + url)
    try:
        response = requests.get(url,timeout = 1,allow_redirects=False)

        with open("C:/Users/IMNU_ADMIN/Desktop/Ŀ���ļ�/{}".format(url.split("/")[-1]), mode="wb") as f:
            f.write(response.content)
            print(format("����ļ���" + url.split("/")[-1]))

    except Exception as e:
        pass