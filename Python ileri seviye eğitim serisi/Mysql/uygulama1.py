from bs4 import BeautifulSoup
import requests
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yusuf2005.",
    database = "shopdb"
)

cursor = db.cursor()

response = requests.get("https://www.trendyol.com/sr?wc=103498&os=1&sk=1")

obj = BeautifulSoup(response.text,"html.parser")
result = obj.select(".prc-box-dscntd")

sql = "INSERT INTO categories (name) VALUES (%s)"

for i in result:
    cursor.execute(sql,tuple(i.text[0]))

db.commit()