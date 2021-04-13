from urllib import request
from http import cookiejar

filename = 'cookie.txt'
# cookie存擋

# MozillaCookieJar儲存cookie
cookie = cookiejar.MozillaCookieJar(filename)
# HTTPCookieProcessor建立cookie處理器
handler = request.HTTPCookieProcessor(cookie)
# 獨立自訂opener
opener = request.build_opener(handler)
# open 開啟網頁
response = opener.open('https://www.104.com.tw')
# 儲存cookie 隱藏
cookie.save(ignore_discard=True,ignore_expires=True)
#
cookie.save()
# cookie讀擋

# 建立MozillaCookieJar物件
cookie = cookiejar.MozillaCookieJar()
# 讀取cookie內容到變數 隱藏
cookie.load(filename, ignore_discard=True, ignore_expires=True)
#
cookie.load(filename)
# HTTPCookieProcessor建立cookie處理器
handler = request.HTTPCookieProcessor(cookie)
# 建立opener
opener = request.build_opener(handler)
# open 開啟網頁
response = opener.open('https://www.104.com.tw')
# 輸出結果
print(cookie)