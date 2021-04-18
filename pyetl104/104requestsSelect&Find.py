import requests,json,time
from urllib import parse
from bs4 import BeautifulSoup

url = 'https://www.104.com.tw/jobs/search/?page='
useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
params = {'keyword':'大數據分析',
          'area':'6001001000'
          }
# 'area':'6001001000台北,6001002000新北'
headers = {'User-Agent':useragent,
           'Referer': 'https://www.104.com.tw'
           }

start_time = time.time()  # 開始時間
count=0
for page in range(1, 5):  # 爬取1-10頁

    res = requests.get(url+str(page), params=params, headers=headers)
    # print(res.url)

    soup = BeautifulSoup(res.content, 'lxml')
    # print(soup)

    jobs = soup.select("#js-job-content > article")
    # print(jobs)

    for row in jobs:
        # data-job-name
        print(row['data-job-name'])
        # data-job-name-link
        print('https:'+row.a['href'])
        # compeny-name
        print(row.ul.a['title'])
        # compeny-link
        print('https:'+row.ul.a['href'])
        # salary
        print(row.find("span", {"class": "b-tag--default"}).getText())
        print('='*60)
        count += 1

print('總共'+str(count)+'個職缺')

print("花費：" + str(time.time() - start_time) + "秒")



    # Id = row['href'][21:26]
#     nextUrl = 'https://www.104.com.tw/job/ajax/content/'+Id
#
#     headers ={'User-Agent':useragent,'Referer':url}
#     res = requests.get(nextUrl, headers=headers)
#     data = json.loads(res.text)
#
#     print(data['data']['header']['custName'])
#     print(data['data']['header']['jobName'])
#     print(data['data']['jobDetail']['jobDescription'])
#     print(data['data']['condition']['workExp'],data['data']['condition']['edu'],data['data']['condition']['major'])
#     print(data['data']['welfare']['welfare'])
#     print(data['data']['contact']['hrName'])
#     print(data['data']['header']['analysisUrl'])

