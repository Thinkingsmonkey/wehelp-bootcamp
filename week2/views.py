from flask import Blueprint
from flask import render_template # 載入 render_template 物件
from flask import request # 載入 request 物件
from flask import jsonify # 載入 jsonify
from flask import redirect, url_for
views1 = Blueprint(__name__, "views1")

@views1.route("/")
def root():
    return "views root page!"

@views1.route("/add")
def add():
    name = "Neal7700185"
    return render_template("add.html", name1=name)
    # 使用物件 render_template，利用 add.html 為模板，修改 name1 為變數 name

@views1.route("/profile/<user>") # 利用 URL 當作參數傳入回應函數
def user(user): # 接收來自連線的參數
    return render_template("add.html", name1=user)

# query parameter
@views1.route("/query")
def query():
    args = request.args
    name = args.get("name")
    age = args.get("age")
    return render_template("add.html", name1=name, age=age)
# 以 ? 開頭，後面放上參數名稱=值，不同參數以 & 相隔
# http://127.0.0.1:8000/views/query?name=Max&age=30

# 回傳 JSON 格式
@views1.route("/json")
def get_json():
    jsonData = {"name": "Neal", "age": 30}
    data = jsonify(jsonData)
    json_data = data.get_json()
    return render_template("add.html", name1=json_data) 
    # 會回傳一個<Response 34 bytes [200 OK]> 的資訊

@views1.route("/goto_google")
def go_to():
    return redirect("https://www.google.com/")

@views1.route("/backto_home")
def backto_home():
    return redirect("/")

# 繼承
@views1.route("/test")
def inherAdd():
    return render_template("test23.html")

# 前後端連線
@views1.route("/sum")
def learn_page():
    return render_template("learn.html")

@views1.route("/calculate", methods=["POST"])
def sum():
    result = 0
    num = int(request.form["num"])
    for x in range(num + 1):
        result += x
    return render_template("learn.html", result=result)
