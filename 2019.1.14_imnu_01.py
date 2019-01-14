import requests
import re

chapterList = []

def getUrl():

    url = "http://www.17k.com/list/2933095.html"

    response = requests.get(url)
    response.encoding = "utf-8"

    aimText = response.text.split("\n")
    for addr in aimText:
        try:

            res = re.match(".*95/(.*?).html",addr)
            res = "http://www.17k.com" + "/chapter/2933095/" + res.group(1) + ".html"
            chapterList.append(res)
        except Exception as e:
            pass

def getText():
    for url in chapterList:
        response = requests.get(url)
        response.encoding = "utf8"
        aimText_totle = response.text

        regex = re.compile("&#12288;&#12288;(.*?)<br /><br />")
        aimText = regex.findall(aimText_totle)
        regex_title = re.compile("<title>(.*?)</title>")
        aimText_title = regex_title.findall(aimText_totle)
        with open("C:/Users/IMNU_ADMIN/Desktop/aimFile/{}.txt".format(aimText_title),mode="w")as f:
            for i in aimText:
                f.write(i + "\r\n\n")

if __name__ == "__main__":
    getUrl()
    getText()
