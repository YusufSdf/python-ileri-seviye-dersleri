import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yusuf2005.",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT COUNT(*) FROM products "
# sql = "SELECT AVG(price) FROM products "
sql = "SELECT MIN(price) FROM products "
sql = "SELECT SUM(price) FROM products "
sql = "SELECT name,price FROM products ORDER BY price"


cursor.execute(sql)

result = cursor.fetchall()

print(result)