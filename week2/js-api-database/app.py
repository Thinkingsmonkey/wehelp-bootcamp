from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/signup", methods=['POST','GET'])
def signup():
    requests = request.get_json()
    con = mysql.connector.connect(
        user="root",
        password="12345678",
        host="localhost",
        database="member"
    )
    cursor = con.cursor()
    cursor.execute('SELECT username, password FROM member WHERE username=%s',( requests["userName"],))
    data = cursor.fetchone()
    print(data != None)

    if data != None:
        con.commit()
        print("資料庫連線成功")
        con.close()
        return "帳號已註冊"
    else:
        cursor.execute('INSERT INTO member(username, password) VALUES(%s, %s) ',( requests["userName"], requests["password"]))
    con.commit()
    print("資料庫連線成功")
    con.close()
    return "註冊成功"
app.run(debug=True)