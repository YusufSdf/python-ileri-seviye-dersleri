from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.yurtlarburada.com/sehirler/ankara-ozel-erkek-ogrenci-yurtlari/")

obj = BeautifulSoup(response.text,"html.parser")
result = obj.select(".DormCard_dorm-card__title-main__463eU")

for i in result:
    print(i.text)