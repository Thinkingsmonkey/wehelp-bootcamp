# 建立留言
def create_message(cursor, data):
    query = "INSERT INTO message (member_id, content) values (%s, %s)"
    cursor.execute(query, (data["id"], data["content"]))


# 取得所有留言
def get_contents(cursor):
    query = "SELECT member.name, message.content, member.username, message.id FROM member INNER JOIN message ON member.id = message.member_id"
    cursor.execute(query)
    return cursor.fetchall()


# 刪除指定留言
def delete_message(cursor, index):
    index = int(index)
    # 利用雙層子查詢直接指定刪除該 row 資料
    query = "DELETE FROM message WHERE id = %s"
    cursor.execute(query, (index,))
    return cursor.rowcount
