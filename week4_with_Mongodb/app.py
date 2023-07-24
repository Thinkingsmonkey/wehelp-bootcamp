from flask import *

# 建立資料庫連線
import pymongo
import sign

client = pymongo.MongoClient(
    "mongodb+srv://root:root123@mycluster.spmsxpm.mongodb.net/?retryWrites=true&w=majority"
)
db = client.member_system  # 建立 member_system 資料庫

app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "secretKey aaa"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/member")
def member():
    if "username" in session:
        message = request.args.get("message", "Welcome")
        return render_template(
            "member.html", message=message, username=session["username"]
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
    # 取得 collection
    collection = db.member
    username = request.form.get("username")
    password = request.form.get("password")
    nickName = request.form.get("nickName")
    data = {"nickName": nickName, "username": username, "password": password}

    # 若 session 以經有 username
    if "username" in session:
        return redirect(url_for("member", message="You are already logged in"))

    # 判斷輸入是否有空值
    if not username or not password:
        message = "Please enter username and password"
        return redirect(url_for("error", message=message))

    # 判斷輸入是否符合條件
    message = sign.signin(data, collection)
    if message == "Congratulations, you have successfully logged in":
        # session 管理登入狀態
        session["username"] = request.form.get("username")
        return redirect(url_for("member", message=message))
    return redirect(url_for("error", message=message))



@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")


@app.route("/signup", methods=["POST"])
def signup():
    # 取得 collection
    collection = db.member
    username = request.form.get("username")
    password = request.form.get("password")
    nickName = request.form.get("nickName")

    data = {"nickName": nickName, "username": username, "password": password}

    # 若 session 以經有 username
    if "username" in session:
        return redirect(url_for("member", message="You are already logged in"))

    # 判斷是否空值
    if not username or not password:
        message = "Please enter username and password"
        return redirect(url_for("error", message=message))

    # 註冊
    message = sign.signup(data, collection)
    if message == "This e-mail has already been registered, please try another one。":
        return redirect(url_for("error", message=message))
    session["username"] = request.form.get("username")
    return redirect(url_for("member", message=message))


app.run(port=3000, debug=True)
