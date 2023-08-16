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
    cursor.execute(query, (data["username"], data["password"]))
    return cursor.fetchone()


# 搜索 memberInfo
def search_member(cursor, username):
    query = "SELECT username, name, id FROM member WHERE username = %s"
    cursor.execute(query, (username,))
    return cursor.fetchone()


# 更新 name
def patch_name(cursor, id, new_name):
    query = "UPDATE member SET name = %s WHERE id = %s"
    cursor.execute(query, (new_name, id))
