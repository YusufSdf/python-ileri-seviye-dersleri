import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yusuf2005.",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "UPDATE products SET name='samsung tab15' WHERE id=3"
sql = "UPDATE products SET name='iphone x',price=price*3 WHERE id=5"

cursor.execute(sql)

db.commit()


