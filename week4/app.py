from flask import *

app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "secretKey aaa"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/member")
def member():
    if "login" in session:
        return render_template("member.html")
    return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("message", "系統報錯，請聯繫客服")
    return render_template("error.html", message=message)


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form.get("username")
    password = request.form.get("password")

    # 判斷輸入是否有空值
    if not username or not password:
        message = "Please enter username and password"
        return redirect(url_for("error", message=message))

    # 判斷輸入是否符合條件
    if username == "test" and password == "test":
        # session 管理登入狀態
        session["login"] = True
        return redirect("member")
    message = "Username or password is not correc"
    return redirect(url_for("error", message=message))


@app.route("/signout")
def signout():
    del session["login"]
    return redirect("/")


@app.route("/square/<num>", methods=["POST"])
def square(num):
    number = int(num)
    answer = number * number
    return render_template("square.html", answer=answer)


app.run(port=3000, debug=True)
