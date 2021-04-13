# 1 import urllib.request
from urllib import request

# 關閉憑證驗證
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://m.manhuagui.com/comic/19785/'

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
headers = {'User-Agant':useragent,
           'Referer':'https://www.104.com.tw',
           'Connection':'keep-alive'}

# 1 res = urllib.request.urlopen(url, data=None, 2)
# res = request.urlopen(url, data=None, 2)

# req = request.Request(url, data=None, headers={}, method=None)
req = request.Request(url, headers=headers)
html = request.urlopen(req).read().decode('utf-8')

print(html)

f = open('html.txt', 'w', encoding='utf8')
f.write(html)
f.close()