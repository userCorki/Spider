import requests_Tools as tools
import pymongo
import threading

def get_Navigation(aim_Num):
    for args in aim_Num:
        try:
            aim_Url = "http://v.7192.com/movie_0_0_0_0_{}".format(args)
            aim_Text = tools.get_Htmltext(aim_Url)
            re_Reresult_List = tools.get_Reresult("class=.thumb.><a href=.(.*?)..target=._blank. title=.(.*?).>",aim_Text)
            for elem in re_Reresult_List:
                final_Url = "http://v.7192.com" + elem[0]
                get_Content(final_Url)
        except:
            pass

def get_Content(final_Url):
    try:
        htmltext = tools.get_Htmltext(final_Url)
        select_result_src = tools.get_Selectresult("#mv_thumb img", htmltext)[0]["data-original"]
        select_result_title = tools.get_Selectresult("#mv_info h2", htmltext)[0].text
        re_result_introduction = str(tools.get_Selectresult("#mv_info p",htmltext)[0].text)
        write_Into_mongo(select_result_src, select_result_title, re_result_introduction)

    except:
        pass

def write_Into_mongo(select_result_src, select_result_title, re_result_introduction):
    try:
        mongo_Connection = pymongo.MongoClient("mongodb://localhost:27017/")
        my_Database = mongo_Connection["Spider"]
        my_Collcetion = my_Database["aim_Text"]
        my_Collcetion.insert({"img_Src":select_result_src,"tiTle":select_result_title,"Introduction":re_result_introduction})
        mongo_Connection.close()
    except:
        pass


if __name__ == "__main__" :

    lock = threading.Lock

    aim_Num = [i for i in range(1,20)]

    get_Navigation(aim_Num)