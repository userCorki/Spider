import requests_Tools as tools

def get_Songname():

    songname_List = []

    for num in range(1, 24):
        try:
            songname_Addr = "https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(num)
            htmltext = tools.get_Htmltext(songname_Addr)
            htmlselect = tools.get_Selectresult("#rankWrap .pc_temp_songlist ul li .pc_temp_songname",htmltext)
            for element in htmlselect:
                songname = element["title"]
                songname_List.append(songname)
        except Exception as e:
            print("get_Songname error !")
    return songname_List

def get_Hash(songname):
    try:
        hush_Textaddr = "http://mobilecdn.kugou.com/api/v3/search/song?format=json&keyword=url{}&page=1&pagesize=20&showtype=1%20---------------------%20%E4%BD%9C%E8%80%85%EF%BC%9A%E5%85%AC%E4%BC%97%E5%8F%B7%E7%81%AB%E7%82%8E%E4%B8%80%E7%AC%91%E5%80%BE%E5%9F%8E%20%E6%9D%A5%E6%BA%90%EF%BC%9ACSDN%20%E5%8E%9F%E6%96%87%EF%BC%9Ahttps://blog.csdn.net/qq_14955245/article/details/79467618%20%E7%89%88%E6%9D%83%E5%A3%B0%E6%98%8E%EF%BC%9A%E6%9C%AC%E6%96%87%E4%B8%BA%E5%8D%9A%E4%B8%BB%E5%8E%9F%E5%88%9B%E6%96%87%E7%AB%A0%EF%BC%8C%E8%BD%AC%E8%BD%BD%E8%AF%B7%E9%99%84%E4%B8%8A%E5%8D%9A%E6%96%87%E9%93%BE%E6%8E%A5%EF%BC%81".format(songname)
        hush_text = tools.get_Htmltext(hush_Textaddr)
        hush = tools.get_Reresult("hash\":\"(.*?)...mvhash",hush_text)[0]
        return hush
    except Exception as e:
        print("get_Hash error !")

def get_Songaddr(hush):
    try:
        songhtml = "http://www.kugou.com/yy/index.php?r=play/getdata&hash={}".format(hush)
        songtext = tools.get_Htmltext(songhtml)
        songaddr = tools.get_Reresult('play_url...(.*?)...authors',songtext)[0]
        return songaddr
    except Exception as e:
        pass

def add_Write(file_Name,text):
    try:
        with open("C:/Users/IMNU_ADMIN/Desktop/{}".format(file_Name),mode="a",encoding="utf8") as f:
            f.write(text + "\n")
    except Exception as e:
        pass


if __name__ =="__main__":

    songname_List = get_Songname()

    for songname in songname_List:
        hash = get_Hash(songname)
        songaddr = get_Songaddr(hash)
        add_Write("kuGou_Music.txt", songname)
        add_Write("kuGou_Music.txt", songaddr)
        text = "\n"
        add_Write("kuGou_Music.txt", text)


