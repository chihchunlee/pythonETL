import requests
from bs4 import BeautifulSoup

r =  requests.get("http://www.google.com.tw")
# encoding
r.encoding="utf8"

with open("./testwrite.txt", "w", encoding="utf8") as fp:
    fp.write(r.text)


# html.parser or lxml  or html5lib
soup = BeautifulSoup(r.text, "lxml")
# soup.prettify()
with open("./testwrite1.txt", "w", encoding="utf8") as fp:
    fp.write(soup.prettify())


# with open("testwrite.txt", "r", encoding="utf8")as fp1:
#     soup1 = BeautifulSoup(fp1, "lxml")
    # print(soup1.prettify())

# bs4.element.Tag
html_str = "<div id='msg' class='body strikeout'>Hello!World <p><!-- test --></p></div>"
soup2 = BeautifulSoup(html_str, "lxml")
tag = soup2.div
print(type(tag))
print(tag.name)
print(tag["id"])
print(tag["class"])
print(tag.attrs)

# bs4.BeautifulSoup
print(soup2.name)
print(type(soup2))

# bs4.element.NavigableString
print(tag.string)
print(type(tag.string))

html_str1 = "<div id='msg' class='body strikeout'>Hello!World! <p> Final Test</p></div>"
soup3 = BeautifulSoup(html_str1, "lxml")
tag1 = soup3.div
print(tag1.string)
print(type(tag1.string))
print(tag1.get_text())
print(tag1.get_text("-"))
print(tag1.get_text("-", strip=True))
print(type(tag1.text))

# bs4.element.Comment
comment = soup2.p.string
print(comment)
print(type(comment))


