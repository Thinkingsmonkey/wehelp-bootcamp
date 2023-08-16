from flask import render_template, redirect, request, session, Blueprint, url_for
from models.db_config import db_pool
import models.member_model as member_model
import models.message_model as message_model
import models.connect_model as connect_model

member_controller = Blueprint("member", __name__)


@member_controller.route("/")
def member():
    if "username" in session:
        message = request.args.get("message", "Welcome")
        connect = connect_model.get_connect(db_pool)
        contents = message_model.get_contents(connect["cursor"])
        connect_model.con_close(connect["con"])
        return render_template(
            "member.html", message=message, name=session["name"], contents=contents
        )
    return redirect("/")


@member_controller.route("/signin", methods=["POST", "GET"])
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
    connect = connect_model.get_connect(db_pool)
    # 檢查帳號密碼、根據結果執行成功或失敗事件
    result = member_model.signin(connect["cursor"], data)
    connect_model.con_close(connect["con"])
    if result != None:
        # session 管理登入狀態
        session["id"] = result[0]
        session["name"] = result[1]
        session["username"] = result[2]
        message = "Congratulations, you have successfully logged in"
        return redirect(url_for("member.member", message=message))
    message = "Username or password is not correc"
    return redirect(url_for("error.error", message=message))


@member_controller.route("/signout")
def signout():
    if "username" in session:
        del session["username"]
    return redirect("/")


@member_controller.route("/signup", methods=["POST"])
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
    connect = connect_model.get_connect(db_pool)
    result = member_model.signup(connect["cursor"], data)
    connect_model.con_close(connect["con"])
    if result == "This e-mail has already been registered, please try another one。":
        return redirect(url_for("error.error", message=result))
    session["id"] = result[0]
    session["name"] = result[1]
    session["username"] = result[2]
    return redirect("/")
