import requests,json,time
import pandas as pd
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

count1 = 0
count2 = 0
for page in range(1, 2):
    count1 += 1
    print('page'+str(count1))

    res1 = requests.get(url + str(page), params=params, headers=headers)
    # print(res.url)

    soup1 = BeautifulSoup(res1.content, 'lxml')
    # print(soup)

    jobs = soup1.select("#js-job-content > article")
    # print(jobs)

    # jobtitles = soup.select('a.js-job-link')
    # jobtitles = soup.select('#js-job-content > article > div.b-block__left > h2 > a')

    # print(jobtitles)
    # ==================================================================
    # for item in jobtitles:
    #     result={
    #         'jobtitle':item.get_text(),
    #         'link':'https:' + item.get('href')
    #     }
    #     print(result)
    # ==================================================================

    items = []
    for row in jobs:
        ID = ('https:'+row.a['href'])[27:32]
        nextUrl = 'https://www.104.com.tw/job/ajax/content/'+ID

        # headers ={'User-Agent':useragent,'Referer':url}
        # headers2 = {'User-Agent': useragent, 'Referer': 'https://www.104.com.tw/job/main/', 'Host': 'www.104.com.tw'}
        res2 = requests.get(nextUrl, headers=headers)

        data = json.loads(res2.text)['data']
        # print(data)

        # terminal
        print('='*60)
        print(data['header']['appearDate'])
        print(data['header']['custName'])
        print(data['header']['custUrl'])
        print(data['header']['jobName'])
        print(data['jobDetail']['salary'])
        print('exp :'+data['condition']['workExp'])
        print('其他:\n'+data['condition']['other'])
        print('工作內容:\n'+data['jobDetail']['jobDescription'])
        count2 += 1
        # in csv
        # date = data['header']['appearDate']
        # companyName = data['header']['custName']
        # companyURL = data['header']['custUrl']
        # jobName = data['header']['jobName']
        # salary = (data['jobDetail']['salary'])
        # exp = data['condition']['workExp']
        # other = data['condition']['other']
        # jobContent = data['jobDetail']['jobDescription']
        #
        # items.append((date,companyName,companyURL,jobName,salary,exp,other,jobContent))

# print(items)

# df = pd.DataFrame(items, columns=['date','companyName', 'companyURL', 'jobName', 'salary', 'exp', 'other', 'jobContent'])

# print(df)

# df.to_csv("teb103_08_李智鈞.csv",index=False,encoding='utf-8')

print()
print()

print('總共'+str(count2)+'個職缺')

print("花費：" + str(time.time() - start_time) + "秒")