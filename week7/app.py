from flask import *

# 建立資料庫連線
import mysql.connector
import mysql.connector.pooling
import mysql_sign

dbconfig = {
    "user": 'root',
    "password": '12345678',
    "host": 'localhost',
    "database": 'website',
    "pool_size": 5,  # 設置連接池大小
}
db_pool = mysql.connector.pooling.MySQLConnectionPool(**dbconfig)

app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "secretKey aaa"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/member")
def member():
    if "username" in session:
        message = request.args.get("message", "Welcome")
        connect = mysql_sign.get_connect(db_pool)
        contents = mysql_sign.get_contents(connect["cursor"])
        mysql_sign.con_close(connect["con"])
        return render_template(
            "member.html", message=message, name=session["name"], contents=contents
        )
    return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("message", "Error, please contact customer service")
    return render_template("error.html", message=message)


@app.route("/square/<num>", methods=["POST"])
def square(num):
    number = int(num)
    answer = number * number
    return render_template("square.html", answer=answer)


@app.route("/signin", methods=["POST"])
def signin():
    # 取得使用者輸入資料
    username = request.form.get("username")
    password = request.form.get("password")
    data = {"username": username, "password": password}

    # 判斷輸入是否有空值
    if not username or not password:
        message = "Please enter username and password"
        return redirect(url_for("error", message=message))
    
    # 建立 cursor 物件
    connect = mysql_sign.get_connect(db_pool)
    # 檢查帳號密碼、根據結果執行成功或失敗事件
    result = mysql_sign.signin(connect["cursor"], data)
    mysql_sign.con_close(connect["con"])
    if result != None:
        # session 管理登入狀態
        session["id"] = result[0]
        session["name"] = result[1]
        session["username"] = result[2]
        message = "Congratulations, you have successfully logged in"
        return redirect(url_for("member", message = message))
    message = "Username or password is not correc"
    return redirect(url_for("error", message = message))


@app.route("/signout")
def signout():
    if "username" in session:
        del session["username"]
    return redirect("/")


@app.route("/signup", methods=["POST"])
def signup():
    # 取得使用者輸入資料
    username = request.form.get("username")
    password = request.form.get("password")
    name = request.form.get("name")
    data = {"name": name, "username": username, "password": password}

    # 判斷是否空值
    if not username or not password:
        message = "Please enter username and password"
        return redirect(url_for("error", message=message))

    # 註冊
    # 建立 cursor 物件
    con = db_pool.get_connection()
    cursor = con.cursor()
    result = mysql_sign.signup(cursor, data)
    con.commit()
    con.close()
    if result == "This e-mail has already been registered, please try another one。":
        return redirect(url_for("error", message = result))
    session["id"] = result[0]
    session["name"] = result[1]
    session["username"] = result[2]
    return redirect("/")


@app.route("/createMessage", methods=["POST", "GET"])
def createMessage():
    content = request.form.get("content")
    if request.method == "POST":
        # 操控數據庫 添加留言
        data = {
            "id": session["id"], 
            "username": session["username"], 
            "name": session["name"], 
            "content": content
        }
        connect = mysql_sign.get_connect(db_pool)
        mysql_sign.createMessage(connect["cursor"], data)
        mysql_sign.con_close(connect["con"])
        return redirect("/createMessage")
    return redirect(url_for("member"))


@app.route("/deleteMessage", methods=["POST", "GET"])
def deleteMessage():
    if request.method == "POST":
        index = request.form.get("index")
        connect = mysql_sign.get_connect(db_pool)
        mysql_sign.deleteMessage(connect["cursor"], index)
        mysql_sign.con_close(connect["con"])
        return redirect("/deleteMessage")
    return redirect("/member")

@app.route("/api/member", methods=["GET", "PATCH"])
def memberAPI():
    if request.method == "GET":
        falseReturn = jsonify({"data":None})
        if "username" not in session:
            return falseReturn, 401
        username = request.args.get("username")
        connect = mysql_sign.get_connect(db_pool)
        data = mysql_sign.search_member(connect["cursor"], username)
        mysql_sign.con_close(connect["con"])
        if data == None:
            return falseReturn, 400
        return jsonify({ "data": {
            "username": data[0],
            "name": data[1],
            "id": data[2],
        }})
    
    if request.method == "PATCH":
        if "username" not in session:
            return jsonify({"error":True, "message": "更新失敗!"}), 401
        newName = request.json.get("name")
        connect = mysql_sign.get_connect(db_pool)
        mysql_sign.patch_name(connect["cursor"], session["id"], newName)
        connect["con"].commit()
        data = mysql_sign.search_member(connect["cursor"], session["username"])
        # 當 member 的 name 被修改後，session 也要一起修改
        mysql_sign.con_close(connect["con"])
        session["id"] = data[2]
        session["name"] = data[1]
        session["username"] = data[0]
        return jsonify({ 
            "ok": True,
            "data": {
            "username": data[0],
            "name": data[1],
            }
        })


app.run(port=3000, debug=True)