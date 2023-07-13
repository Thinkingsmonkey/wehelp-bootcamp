from flask import Flask, url_for # 載入 flask
from views import views1 # 從黨名 views 中載入 views1 物件
from flask import redirect
app = Flask(__name__) # 建立 Application 物件
app.register_blueprint(views1, url_prefix="/views")

@app.route("/") # 建立路徑裝飾器，首頁("/")
def home(): # 連線後的回應函式
    return "This is Home Page!!!!!!" # 回應的內容


app.run(debug=True, port="8000") # 啟動伺服器 (上方所有的路徑回應)