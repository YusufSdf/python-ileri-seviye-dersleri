import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yusuf2005.",
    database = "shopdb"
)

cursor = db.cursor()

sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"

values = [  ("iphone 15", 40000, "3.jpg", "nice"),
            ("samsung s25", 45000, "4.jpg", "nice"),
            ("iphone 15 pro", 55000, "5.jpg", "nice"),
        ]

cursor.executemany(sql,values)


db.commit()
print(cursor.rowcount)
print(values)