from bs4 import BeautifulSoup

with open("index.html",encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html,"html.parser")
result = obj
result = obj.title
result = obj.title.string
result = obj.body.h1.string.strip()
result = obj.div.h2
result = obj.find_all("div")

result = obj.select(".item") # class ı item olanlar
print(result)

