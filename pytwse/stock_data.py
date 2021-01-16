from bs4 import BeautifulSoup
import requests
import json,csv

url = 'https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market=1&issuetype=1&industry_code=&Page=1&chklike=Y'
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
headers = {'User-Agent': useragent}

item = list()

source = requests.get(url, headers=headers)
soup = BeautifulSoup(source.text, 'lxml')

blocks = soup.find_all("table",{"class":"h4"})
for block in blocks:                                     #.定位區塊
    datas = block.find_all("tr")
    del(datas[0])                                        #.標題列刪除
    for data in datas:
        intnstockNo = data.find_all("td")[1].text        #.國際證券編碼
        stockNumber = int(data.find_all("td")[2].text)     #.有價證券代號
        stockCompeny = data.find_all("td")[3].text       #.有價證券名稱
        stockMkt = data.find_all("td")[4].text           #.市場別
        stocktype = data.find_all("td")[5].text          #.有價證券別
        stockindustry = data.find_all("td")[6].text      #.產業別
        stockinMkt = data.find_all("td")[7].text         #.公開發行/上市(櫃)/發行日
        stockCFI = data.find_all("td")[8].text           #.CFICode

        items = [
            intnstockNo,stockNumber,stockCompeny,stockMkt,stocktype,stockindustry,stockinMkt,stockCFI
        ]
        item.append(items)

#.stockallData
        # items = {
        #
        #     "產業別":stockindustry,
        #     "公開發行/上市(櫃)/發行日":stockinMkt,
        #     "國際證券編碼":intnstockNo,
        #     "有價證券代號":stockNumber,
        #     "有價證券名稱":stockCompeny,
        #     "市場別":stockMkt,
        #     "有價證券別":stocktype,
        #     "CFICode":stockCFI
        # }
        # item.append(items)

#.stockonlyNumber
        # item.append(stockNumber)

with open("stockalldata.json",'w',encoding="utf-8") as fp:
   json.dump(item,fp)

#.csv.file

# with open("stockallData.csv",'w+',newline='',encoding="utf-8") as fp:
#     writer = csv.writer(fp)
#     writer.writerow(["國際證券編碼","有價證券代號","有價證券名稱","市場別","有價證券別","產業別","公開發行/上市(櫃)/發行日","CFICode"])
#     for row in item:
#         writer.writerow(row)

#.csv.file

# with open("stockID.csv",'w+',newline='',encoding="utf-8") as fp:
#     writer = csv.writer(fp)
#     writer.writerow([item])



