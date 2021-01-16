from bs4 import BeautifulSoup
import requests
import re
import time
import csv

url = 'https://search.ltn.com.tw/list?keyword=%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E&start_time=20190101&end_time=20201231'

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
headers = {'User-Agent': useragent}

source = requests.get(url, headers=headers)
soup = BeautifulSoup(source.text, 'lxml')
titles = soup.select("#ec > section > div.page-name > ul > li > div > a.tit")
links = soup.select("#ec > section > div.page-name > ul > li > div > a.http")
keylist =[]

for title in titles:
    titleslist = title.text
    keylist.append(titleslist)
valuelist = []
for link in links:
    newurl = link.text
    # print(newurl)
    source2 = requests.get(newurl)
    soup2 = BeautifulSoup(source2.text, 'lxml')
    # print(soup2)

    contents = soup2.select("p")
    for content in contents:
        contentlist = content.text.replace(' ', '').replace('\n', '')
        # valuelist.append(contentlist)
        print(contentlist)
# print(type(valuelist))

# datadict = dict(zip(keylist,valuelist))
# print(datadict)
# valuelistF = list(filter(None, valuelist))
# valuelistF = []
# for i in valuelist:
#     re.sub(r"\s+", "", i)

# print(valuelist)



