from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.trendyol.com/sr?wc=103498&os=1&sk=1")

obj = BeautifulSoup(response.text,"html.parser")
result = obj.select(".prc-box-dscntd")
liste = []

for i in result:
    liste.append(i.text[0])
    print(i.text)
print(liste)