import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yusuf2005.",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT name,categoryId FROM products"
# sql = "SELECT name FROM categories"
sql = "SELECT products.name, categories.name FROM products INNER JOIN categories ON products.categoryId=categories.id"

cursor.execute(sql)

result = cursor.fetchall()

print(result)