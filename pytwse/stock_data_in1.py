import twstock
import time
import random
import csv
import json
# csvfile = "2330.csv"
# start = time.time()
# #
# stock = twstock.Stock('2330')
# for y in range(2020,2021):
#     for m in range(1,13):
#         data = stock.fetch(y,m)
#         time.sleep(random.randint(6,10))

#         with open("2330_"+str(y)+".csv",'a+',newline='') as fp:
#             writer = csv.writer(fp)
#             writer.writerow(["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"])
#             for row in data:
#                 writer.writerow(row)
#
#         print("2330_"+str(y)+"_"+str(m)+"done")
# end = (time.time()-start)
# print("Time used:",end)

# csvfile = "2330.csv"
# with open(csvfile,'w+',newline='') as fp:
#     writer = csv.writer(fp)
#     writer.writerow(["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"])
#     for row in data:
#         writer.writerow(row)

# print(data)

datalist = list()
with open("bmstockno.csv",newline='',encoding='utf-8') as fp:
    rows = csv.reader(fp)
    for row in rows:
        datalist.append(int(row[0]))
    print(datalist)

# for sNo in data:
#     stock = twstock.Stock(sNo)
#     data = stock.fetch_from(2010, 1)

# import csv
#
# # 開啟 CSV 檔案
# with open(r'C:\Users\DA01008\Desktop\STOCK_DAY_2330_201601.csv', newline='') as csvfile:
#
#   # 讀取 CSV 檔案內容
#   rows = csv.reader(csvfile)
#
#   # 以迴圈輸出每一列
#   for row in rows:
#     print(row)