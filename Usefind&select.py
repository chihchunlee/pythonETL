import requests
from bs4 import BeautifulSoup

# find
tag_a = soup.find("a")
print(tag_a.string)

tag_p = soup.find(name="p")
tag_a = tag_p.find(name="a")
# print(tag_p.a.string) == print(tag_a.string)

# 指定 css class = score 用 attrs
# tag_span = soup.find(attrs={"class":"score"}) == tag_span = soup.find(class_="score")
print(tag_span.string)
# 指定 text 有 男
tag_str = soup.find(text="男")

#  limit 前幾筆
tag_list = soup.find_all("p", class_="question", limit=2)
# find_all(True) 搜尋之下所有標籤
tag_list = soup.find_all(True)
# find_all(text=True) 搜尋之下所有文字
tag_list = soup.find_all(text=True)
# 找出指定文字內容
tag_list = soup.find_all(text=["20","40"])
# 找出所有 p 或 span
tag_list = soup.find_all("p","span")

# select
tag_title = soup.select("title")
tag_title = soup.select("html head title")
print(tag_title[0].string)
tag_link = soup.select("body div a")
print(tag_link)
# 找出所有 p 的子標籤是 a 的
tag_link = soup.select("p > a")
# 找出所有 ul 的子標籤是 li 的 且只取第二個 :nth-of-type(2)
tag_li = soup.select("ul > li:nth-of-type(2)")
# 找出所有 div 的子標籤  id 是 email 的
tag_span = soup.select("div > #email")

# #是id ~ 搜尋之後所有的 .是class
tag_span = soup.select("#q1 ~ .survey")
#       + 只搜尋第一個符合 .survey
tag_span = soup.select("#q1 + .survey")
# 只搜尋標籤span中id是q1的
tag_span = soup.select("span#q1")
# 多個id
tag_span = soup.select("#q1, #q2")
# ^ 開頭
tag_span = soup.select("a[href^='http://']")
# $ 結尾
tag_span = soup.select("a[href$='q3']")
# * 中間包含
tag_span = soup.select("a[href*='q']")

# select_one 只找第一筆 其餘用法一樣

