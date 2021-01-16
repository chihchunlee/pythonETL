import requests,json,csv
import pandas as pd
from bs4 import BeautifulSoup

# csvfile = 'teb103_08_李智鈞.csv'

for page in range(1,5):
    url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword=%E5%A4%A7%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=1&asc=0&page='+ str(page) +'&mode=s&jobsource=2018indexpoc'
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    headers = {'User-Agent':useragent}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    # jobtitles = soup.select('a[class="js-job-link"]')
    jobtitles = soup.select('#js-job-content > article > div.b-block__left > h2 > a')
    # 定位 copy copy selector #js-job-content > article:nth-child(19) > div.b-block__left > h2 > a
    # 去除疑似參數的部分 :nth-child(19)
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
    for row in jobtitles:
        # print(item.text)
        # print('https:'+item.get('href'))
        Id = row['href'][21:26]
        # print(Id)

        nextUrl = 'https://www.104.com.tw/job/ajax/content/'+Id
        # headers ={'User-Agent':useragent,'Referer':'https://www.104.com.tw/job/main/','Host':'www.104.com.tw'}
        headers ={'User-Agent':useragent,'Referer':url}
        res = requests.get(nextUrl, headers=headers)
        data = json.loads(res.text)
        # print(data)
        companyName = data['data']['header']['custName']
        # print(data['data']['header']['custName'])
        jobName = data['data']['header']['jobName']
        # print(data['data']['header']['jobName'])
        jobContent = data['data']['jobDetail']['jobDescription']
        # print(data['data']['jobDetail']['jobDescription'])
        request = data['data']['condition']['workExp'],data['data']['condition']['edu'],data['data']['condition']['major']
        # print(data['data']['condition']['workExp'],data['data']['condition']['edu'],data['data']['condition']['major'])
        welfare = data['data']['welfare']['welfare']
        # print(data['data']['welfare']['welfare'])
        jobcontact = data['data']['contact']['hrName']
        # print(data['data']['contact']['hrName'])
        joburl = 'http:'+data['data']['header']['analysisUrl']
        # print(data['data']['header']['analysisUrl'])

        items.append((companyName,jobName,jobContent,request,welfare,jobcontact,joburl))

# print(items)

            # item = []
        # item.append(companyName)
        # item.append(jobName)
        # item.append(jobContent)
        # item.append(request)
        # item.append(welfare)
        # item.append(jobcontact)
        # item.append(joburl)
        # items.append(item)


        # print(item)
        # items.append(item)
        # print(items)

        df = pd.DataFrame(items, columns=['companyName', 'jobName', 'jobContent','request','welfare','jobcontact','joburl'])
    # print(df)

        df.to_csv("teb103_08_李智鈞.csv",index=False,encoding='utf-8')



    # try:
    #     with open(csvfile,'w+')as fp:
    #         writer = csv.writer(fp)
    #         writer.writerow(['companyName', 'jobName', 'jobContent','request','welfare','jobcontact','joburl'])
    #         for item in items:
    #             writer.writerow(item)
    # except:
    #     pass

    # pddata = {'companyName':[companyName],
    #               'jobName':[jobName],
    #            'jobContent':[jobContent],
    #               'request':[request],
    #               'welfare':[welfare],
    #            'jobcontact':[jobcontact],
    #                'joburl':[joburl]
    # }
    #
    # df = pd.DataFrame(pddata)
    # print(df)

    # columns = ['companyName', 'jobName', 'jobContent','request','welfare','jobcontact','joburl']
    # datapd = [
    #     [companyName],
    #     [jobName],
    #     [jobContent],
    #     [request],
    #     [welfare],
    #     [jobcontact],
    #     [joburl]
    # ]
    #
    # df = pd.DataFrame(data=datapd, columns=columns)
    # print(df)

    # df = pd.DataFrame(columns=['companyName', 'jobName', 'jobContent','request','welfare','jobcontact','joburl'])
    # df.loc[0] = [companyName, jobName]







    # with open('f.txt', 'w') as f:
    #     f.write(data)







    # data = res.json()
    # print(data['data'])
    # print(type(data))
    # # print(data['metadata'].keys())
    # htmlStr = data['data']
    # # print(htmlStr)
    # soup = BeautifulSoup(htmlStr, 'lxml')









