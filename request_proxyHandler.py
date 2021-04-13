from urllib import request

url = 'https://www.104.com.tw'

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
headers = {'User-Agant':useragent,
           'Referer':'https://www.104.com.tw',
           'Connection':'keep-alive'}
# 設定代理ip
proxy_handler = request.ProxyHandler({
    'http':'218.56.132.157:8080',
    'https':'183.30.197.29:9797'})

# 使用build_opener來建立代理ip的opener物件
opener = request.build_opener(proxy_handler)

res = opener.open(url)
html = res.read().decode('utf-8')

# print(html)

f = open('html.txt', 'w', encoding='utf8')
f.write(html)
f.close()