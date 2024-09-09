import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yusuf2005.",
    database = "shopdb"
)

cursor = db.cursor()

sql = "SELECT * from products WHERE id >=1 and price = 55000"

cursor.execute(sql)
result = cursor.fetchall()

print(result)