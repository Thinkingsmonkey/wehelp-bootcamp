import mysql.connector

con = mysql.connector.connect(
    user = 'root',
    password = '12345678',
    host = 'localhost',
    database = 'website'
)

cursor = con.cursor()
index = 2
query = f"SELECT id FROM message  ORDER BY id LIMIT {index-1},1"
cursor.execute(query)
data = cursor.fetchone()
# query = f'DELETE FROM message ORDER BY id LIMIT {index}'
# cursor.execute(query)
print(data[0])

con.commit()
con.close()