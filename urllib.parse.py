from urllib import parse
from urllib import request
#
# url=''
# data = {
#     'value':'true',
# }
# # 資料處理
# data = parse.urlencode(data).encode('utf-8')
# req = request.urlopen(url, data=data)

# 解碼
url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword=Python%20%E8%B3%87%E8%A8%8A%E5%B7%A5%E7%A8%8B&expansionType=area,spec,com,job,wf,wktm&jobsource=2018indexpoc'
f = parse.unquote(url)
print(f)
# 編碼
s = parse.quote(f)
print(s)