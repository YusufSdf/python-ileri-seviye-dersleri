import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yusuf2005.",
    database = "shopdb"
)

cursor = db.cursor()
# cursor.execute("CREATE DATABASE tester1")
cursor.execute("CREATE TABLE categories (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45))")
cursor.execute("SHOW TABLES")

for i in cursor:
    print(i)
