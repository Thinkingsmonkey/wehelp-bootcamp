import urllib.request as req
import time
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
import bs4
import threading


def get_bs4_root(url):
    request = req.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        },
    )
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    page_root = bs4.BeautifulSoup(data, "html.parser")
    return page_root


def get_next_page_url(page_root):
    return pttHost + page_root.find("a", class_="btn wide", string="‹ 上頁").get("href")


def write_page_row(page_root):
    #
    page_titles = page_root.find_all("div", class_="title")
    page_tweets = page_root.find_all("div", class_="nrec")
    page_titleList = []
    page_tweetList = []
    title_page_timeList = []
    threads = []

    for index, page_title in enumerate(page_titles):
        if page_title.a == None:
            continue
        # page_titleList
        page_titleList.append(page_title.a.string)

        # page_tweetList
        if page_tweets[index].span == None:
            page_tweetList.append("")
        else:
            page_tweetList.append(page_tweets[index].span.string)

        # title_page_timeList
        threads.append(
            threading.Thread(target=timeList, args=(page_title, title_page_timeList))
        )
    # 子執行開始與等待結束要分開
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    for num in range(len(page_titleList)):
        row.append(
            f"{page_titleList[num]},{page_tweetList[num]},{title_page_timeList[num]}\n"
        )


def timeList(page_title, title_page_timeList):
    title_link = pttHost + page_title.a.get("href")
    title_page_root = get_bs4_root(title_link)
    title_page_values = title_page_root.find_all("span", class_="article-meta-value")
    title_page_time = title_page_values[-1].string
    title_page_timeList.append(title_page_time)


search_num = 3
url = "https://www.ptt.cc/bbs/movie/index.html"
pttHost = "https://www.ptt.cc"
row = []
for i in range(0, search_num):
    print(i)
    # 取得 當前頁 bs4-root
    page_root = get_bs4_root(url)
    # 找出 title、tweet、time
    start = time.time()
    write_page_row(page_root)
    end = time.time()
    print("Time：", end - start, "seconds")
    # 取得下一頁網址
    url = get_next_page_url(page_root)


with open("movie.txt", "w", encoding="utf-8", newline="") as file:
    for r in row:
        file.write(r)
