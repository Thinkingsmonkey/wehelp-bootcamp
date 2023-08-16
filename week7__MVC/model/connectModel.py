# 建立連線
def get_connect(db_pool):
    con = db_pool.get_connection()
    return {"con":con, "cursor":con.cursor()}

# 結束連線
def con_close(con):
    con.commit()
    con.close()
