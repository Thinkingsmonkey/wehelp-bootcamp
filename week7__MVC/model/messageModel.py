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