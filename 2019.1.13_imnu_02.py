import requests

response = requests.get("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808")

aimText_addr = response.text.split("\r\n")

for url in aimText_addr:
    print("正在访问地址：" + url)
    try:
        response = requests.get(url,timeout = 1,allow_redirects=False)

        with open("C:/Users/IMNU_ADMIN/Desktop/目标文件/{}".format(url.split("/")[-1]), mode="wb") as f:
            f.write(response.content)
            print(format("输出文件：" + url.split("/")[-1]))

    except Exception as e:
        pass