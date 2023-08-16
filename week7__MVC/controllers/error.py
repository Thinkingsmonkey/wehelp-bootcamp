from flask import render_template, request,Blueprint
# ! error 裝飾器 404、500 chatGPT

errorCtrlr = Blueprint("error", __name__)

@errorCtrlr.route("/")
def error():
    message = request.args.get("message", "Error, please contact customer service")
    return render_template("error.html", message=message)