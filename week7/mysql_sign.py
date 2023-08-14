# 建立連線
def get_connect(db_pool):
    con = db_pool.get_connection()
    return {"con":con, "cursor":con.cursor()}

# 結束連線
def con_close(con):
    con.commit()
    con.close()

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
    query = "SELECT member.name, message.content, member.username FROM member INNER JOIN message ON member.id = message.member_id"
    cursor.execute(query)
    return cursor.fetchall()

# 刪除指定留言
def deleteMessage(cursor, index):
    index = int(index)
    # 利用雙層子查詢直接指定刪除該 row 資料
    query = 'DELETE FROM message WHERE id IN (SELECT id FROM (SELECT id FROM message ORDER BY id LIMIT %s,1)a);'
    cursor.execute(query, (index-1,))
    return "OK"

# 搜索 memberInfo
def search_member(cursor, username):
    query = "SELECT username, name, id FROM member WHERE username = %s"
    cursor.execute(query,(username,))
    return cursor.fetchone()

# 更新 name
def patch_name(cursor, id, newName):
    query = "UPDATE member SET name = %s WHERE id = %s"
    cursor.execute(query, (newName, id))
    