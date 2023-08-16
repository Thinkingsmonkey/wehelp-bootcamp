from flask import render_template, redirect, request, session, Blueprint, url_for
from model.dbConfig import db_pool
import model.memberModel as memberModel
import model.messageModel as messageModel
import model.connectModel as connectModel

memberCtrlr = Blueprint("member", __name__)

@memberCtrlr.route("/")
def member  ():
    if "username" in session:
        message = request.args.get("message", "Welcome")
        connect = connectModel.get_connect(db_pool)
        contents = messageModel.get_contents(connect["cursor"])
        connectModel.con_close(connect["con"])
        return render_template(
            "member.html", message=message, name=session["name"], contents=contents
        )
    return redirect("/")


@memberCtrlr.route("/signin", methods=["POST", "GET"])
def signin():
    # 取得使用者輸入資料
    username = request.form.get("username")
    password = request.form.get("password")
    data = {"username": username, "password": password}

    # 判斷輸入是否有空值
    if not username or not password:
        message = "Please enter username and password"
        return redirect(url_for("error.error", message=message))
    
    # 建立 cursor 物件
    connect = connectModel.get_connect(db_pool)
    # 檢查帳號密碼、根據結果執行成功或失敗事件
    result = memberModel.signin(connect["cursor"], data)
    connectModel.con_close(connect["con"])
    if result != None:
        # session 管理登入狀態
        session["id"] = result[0]
        session["name"] = result[1]
        session["username"] = result[2]
        message = "Congratulations, you have successfully logged in"
        return redirect(url_for("member.member", message = message))
    message = "Username or password is not correc"
    return redirect(url_for("error.error", message = message))


@memberCtrlr.route("/signout")
def signout():
    if "username" in session:
        del session["username"]
    return redirect("/")


@memberCtrlr.route("/signup", methods=["POST"])
def signup():
    # 取得使用者輸入資料
    username = request.form.get("username")
    password = request.form.get("password")
    name = request.form.get("name")
    data = {"name": name, "username": username, "password": password}

    # 判斷是否空值
    if not username or not password:
        message = "Please enter username and password"
        return redirect(url_for("error.error", message=message))

    # 註冊
    # 建立 cursor 物件
    connect = connectModel.get_connect(db_pool)
    result = memberModel.signup(connect["cursor"], data)
    connectModel.con_close(connect["con"])
    if result == "This e-mail has already been registered, please try another one。":
        return redirect(url_for("error.error", message = result))
    session["id"] = result[0]
    session["name"] = result[1]
    session["username"] = result[2]
    return redirect("/")
