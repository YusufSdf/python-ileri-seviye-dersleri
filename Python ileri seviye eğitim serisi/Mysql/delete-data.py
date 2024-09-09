import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yusuf2005.",
    database = "shopdb"
)

cursor = db.cursor()

# sql =   "DELETE FROM products WHERE id=5"
# sql =   "DELETE FROM products WHERE name LIKE '%mega%' "
sql = "DELETE FROM categories"

cursor.execute(sql)
db.commit()


print(f"{cursor.rowcount} tane kayıt silindi")
