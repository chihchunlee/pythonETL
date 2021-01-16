import requests,json
from bs4 import BeautifulSoup

url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword=%E5%A4%A7%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=1&asc=0&page=1&mode=s&jobsource=2018indexpoc'
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
headers = {'User-Agent':useragent}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

jobtitles = soup.select('#js-job-content > article > div.b-block__left > h2 > a')


for row in jobtitles:

    Id = row['href'][21:26]
    nextUrl = 'https://www.104.com.tw/job/ajax/content/'+Id

    headers ={'User-Agent':useragent,'Referer':url}
    res = requests.get(nextUrl, headers=headers)
    data = json.loads(res.text)

    print(data['data']['header']['custName'])
    print(data['data']['header']['jobName'])
    print(data['data']['jobDetail']['jobDescription'])
    print(data['data']['condition']['workExp'],data['data']['condition']['edu'],data['data']['condition']['major'])
    print(data['data']['welfare']['welfare'])
    print(data['data']['contact']['hrName'])
    print(data['data']['header']['analysisUrl'])

