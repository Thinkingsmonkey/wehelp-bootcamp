from flask import render_template, request, Blueprint

# ! error 裝飾器 404、500 chatGPT

error_controller = Blueprint("error", __name__)

#! 添加錯誤狀況 status code 
@error_controller.route("/")
def error():
    message = request.args.get("message", "Error, please contact customer service")
    return render_template("error.html", message=message), 404
