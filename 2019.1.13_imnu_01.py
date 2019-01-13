import requests

url = "http://zyk.bjhd.gov.cn/zwdt/hdyw/index"

header = {      #使用header头
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
}

for i in range(0,50):
    if i == 0:
        request = requests.get(url + ".shtml", headers=header)
        request.encoding = "g12138"         #G12138解码
        cont = request.text

    else:
        url_aim = url + '_' + str(i) + ".shtml"
        request = requests.get(url_aim,headers = header)
        request.encoding = "g12138"
        cont = request.text

    with open("C:/Users/IMNU_ADMIN/Desktop/新建文本文档.txt",mode="a") as f:      #"a"在文本末端追加
        f.write(cont)
