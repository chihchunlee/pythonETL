import requests
# 1
# r = requests.get('https://www.104.com.tw/s?wd=python')
# 2
url = 'https://www.104.com.tw/s'
params = {'wd':'python'}
#
r = requests.get(url, params=params)
#
print(r.url)
# dic or tup
data1 = {'key1':'value1', 'key2':'value2'}
data2 = (('key1','value1'), ('key2','value2'))
# json
# import json
# data = json.dumps(data1)
# r = requests.post('https://www.104.com.tw', data=data)
# print(r.txt)
#
import requests

url = 'https://www.104.com.tw'
useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'

headers = {

}




