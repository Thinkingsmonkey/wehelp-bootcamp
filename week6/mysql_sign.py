# 註冊帳號
def signup(cursor, data):
    # 檢查是否已存在此帳號
    checked = check_member(cursor, data)
    if checked:
        return "This e-mail has already been registered, please try another one。"
    return insert(cursor, data)

# 添加帳號
def insert(cursor, data):
    query = "INSERT INTO member (name, username, password) values (%s, %s, %s)"
    cursor.execute(query, (data["name"], data["username"], data["password"]))
    return signin(cursor, data)
    
# 檢查是否存在此帳號
def check_member(cursor, data):
    query = "SELECT 1 FROM member WHERE username = %s LIMIT 1"
    cursor.execute(query, (data["username"],))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False
    
# 登入帳號
def signin(cursor, data):
    query = "SELECT * FROM member WHERE username = %s AND password = %s"
    cursor.execute(query,(data["username"], data["password"]))
    return cursor.fetchone()

# 建立留言
def createMessage(cursor, data):
    query = "INSERT INTO message (member_id, content) values (%s, %s)"
    cursor.execute(query, (data["id"], data["content"]))

# 取得所有留言
def get_contents(cursor):
    query = "SELECT member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id"
    cursor.execute(query)
    return cursor.fetchall()

# 刪除指定留言
def deleteMessage(cursor, index):
    index = int(index)
    # 法一：
    # # 找出此 index 對應的 message id
    # query = f"SELECT id FROM message ORDER BY id LIMIT {index-1},1"
    # cursor.execute(query)
    # data = cursor.fetchone()
    # # 利用 message id 刪除該留言
    # query = f'DELETE FROM message WHERE id = {data[0]}'
    # 法二：
    # # 利用雙層子查詢直接指定刪除該 row 資料
    query = 'DELETE FROM message WHERE id IN (SELECT id FROM (SELECT id FROM message ORDER BY id LIMIT %s,1)a);'
    cursor.execute(query, (index-1,))
    return "OK"
