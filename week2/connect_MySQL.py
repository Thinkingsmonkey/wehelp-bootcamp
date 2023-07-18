import mysql.connector
# 給予資訊讓 python 連線到指定資料庫
con = mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="mydb"
)

print("資料庫連線成功")
# 取得多筆資料
cursor = con.cursor()
cursor.execute("SELECT * FROM product")
data = cursor.fetchall()
print(data)
for row in data:
    print(row[0], row[1])
con.commit()

# 取得 MySQL 資料，單一筆
# cursor = con.cursor()
# cursor.execute("SELECT * FROM product WHERE id=3")
# data = cursor.fetchone()
# print(data)
# con.commit()

# 更新資料
# productName = "芝芝芒果多多綠"
# cursor = con.cursor()
# cursor.execute("INSERT INTO product(name) VALUES(%s)", (productName,))
# con.commit()

# 關閉
con.close()