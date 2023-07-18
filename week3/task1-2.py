import urllib.request as req
import json
import csv
import re
#Task1：
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(src) as response:
    data = json.load(response)
# 景點名稱,區域,經度,緯度,第⼀張圖檔網址
with open("attraction.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    attractions = data["result"]["results"]
    for info in attractions:
        img = info["file"]
        # 利用 正則表達式 中 (?i) 與 () 分組，把 .jpg 與 .JPG 都抓出，再將副檔名補回去
        imgLink = re.split(r'(?i)(\.jpg)', img)
        imgLink = imgLink[0]+ imgLink[1]
        attraction = [info["stitle"], info["address"][5:8], info["longitude"], info["latitude"], imgLink]
        writer.writerow(attraction)


mrtList = []
mrtCSV = []
for item in attractions:
    if item["MRT"] not in mrtList:
        mrtList.append(item["MRT"])

# 使用 for in enumerate(mrtList) 中個別 mrtStation 
# 先創建一個 mrtCSV list 放入當前 mrtStation
# 當前 mrtStation 與 attractions 中的所有  item["MRT"] 相比，若有相等
# 放進 mrtCSV list 中
# 每跑完一個 mrtStation 就寫入 csv 當中
with open("mrt.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for num, mrtStation in enumerate(mrtList):
        # 設定陽明山國家公園 MRT 為 null 的狀況
        if mrtStation == None:
            mrtCSV.append(["null"])
        else:
            mrtCSV.append([mrtStation])
        for item in attractions:
            if item["MRT"] == None and mrtCSV[num][0] == "null":
                mrtCSV[num].append(item["stitle"])
            if item["MRT"] == mrtCSV[num][0]:
                mrtCSV[num].append(item["stitle"])
        writer.writerow(mrtCSV[num])


# #Task2：
# import bs4
# url = "https://www.ptt.cc/bbs/movie/index.html"
# request = req.Request(url, headers={
#     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
# })

# pttHost = "https://www.ptt.cc"
# with req.urlopen(request) as response:
#     page1_data = response.read().decode("utf-8")

# row = []
# def write_page_row(page_data):
#     # 
#     page_root = bs4.BeautifulSoup(page_data, "html.parser")
#     page_titles = page_root.find_all("div", class_="title")
#     page_tweets = page_root.find_all("div", class_="nrec")
#     page_titleList = []
#     page_tweetList = []
#     title_page_timeList =[]
#     for index, page_title in enumerate(page_titles):
#         if page_title.a == None: continue
#         # page_titleList
#         page_titleList.append(page_title.a.string)
        
#         # page_tweetList
#         if page_tweets[index].span == None:
#             page_tweetList.append("")
#         else:
#             page_tweetList.append(page_tweets[index].span.string)

#         # title_page_timeList
#         timeList(page_title, title_page_timeList)

#     for num in range(len(page_titleList)):
#         row.append( f'{page_titleList[num]},{page_tweetList[num]},{title_page_timeList[num]}\n')

# def timeList(page_title, title_page_timeList):
#     title_link = pttHost + page_title.a.get("href")
#     request.full_url = title_link
#     with req.urlopen(request) as response:
#         title_page_data = response.read().decode("utf-8")
#     title_page_root = bs4.BeautifulSoup(title_page_data, "html.parser")
#     title_page_values = title_page_root.find_all("span", class_="article-meta-value")
#     title_page_time = title_page_values[-1].string
#     title_page_timeList.append(title_page_time)

# def get_next_page_data(page_data):
#     page_root = bs4.BeautifulSoup(page_data, "html.parser")
#     next_page_link = pttHost + page_root.find("a", class_="btn wide", string="‹ 上頁").get("href")
#     request.full_url = next_page_link
#     with req.urlopen(request) as response:
#         data = response.read().decode("utf-8")
#     return data

# write_page_row(page1_data)
# page2_data = get_next_page_data(page1_data)
# write_page_row(page2_data)
# page3_data = get_next_page_data(page2_data)
# write_page_row(page3_data)
# with open("movie.txt", "w", encoding="utf-8", newline="") as file:
#     for r in row:
#         file.write(r)
