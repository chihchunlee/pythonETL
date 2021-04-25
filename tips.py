import requests

r = requests.get("http://www.google.com")


# 改編碼
# r.encoding="big5"

# 查狀態碼
print(r.status_code)
print(r.status_code == requests.codes.ok)
print(r.status_code == requests.codes.all_good)

# 取得標頭 內容型態 內容長度 日期 伺服器名稱
print(r.headers['Content-Type'])
print(r.headers['Content-Length'])
print(r.headers['Date'])
print(r.headers['Server'])

# 如上一樣的方法 headers.get
print(r.headers.get('Content-Type'))
print(r.headers.get('Content-Length'))
print(r.headers.get('Date'))
print(r.headers.get('Server'))

# cookies
url='http://httpbin.org/cookies'
cookies=dict(name='chris')
v = requests.get(url, cookies=cookies)
print(v.text)

# try-except
try:
    r1 = requests.get("http://www.google.com", timeout=0.03)
    print(r1.text)
except requests.exceptions.Timeout:
    print('T')
except requests.exceptions.RequestException:
    print('RE')
except requests.exceptions.HTTPError:
    print('HE')
except requests.exceptions.ConnectionError:
    print('CE')

# open close 不會自動關閉 write
fp = open("testwrite.txt", "w", encoding="utf8")
fp.write(r.text)
print("sucess")
fp.close()

# read
# fp = open("testwrite.txt", "r", encoding="utf8")
# str = fp.read()
# print("sucess")
# print(str)

# with open 自動關閉
# with open("testwrite.txt", "r", encoding="utf8") as fp:
#     str = fp.read()
#     print(str)

with open("testwrite.txt", "r", encoding="utf8") as fp:
    list1 = fp.readlines()
    for line in list1:
        print(line, end="")