from flask import Blueprint, request, session, redirect, url_for
from model.dbConfig import db_pool
import model.memberModel as memberModel
import model.messageModel as messageModul
import model.connectModel as connectModel


messageCtrlr = Blueprint("message", __name__)

@messageCtrlr.route("/", methods=["POST", "GET"])
def createMessage():
    if request.method == "POST":
      content = request.form.get("content")
        # 操控數據庫 添加留言
      data = {
          "id": session["id"], 
          "username": session["username"], 
          "name": session["name"], 
          "content": content
      }
      connect = connectModel.get_connect(db_pool)
      messageModul.createMessage(connect["cursor"], data)
      connectModel.con_close(connect["con"])
      return redirect("/message")
    return redirect(url_for("member.member"))



@messageCtrlr.route("/del", methods=["POST", "GET"])
def deleteMessage():
    if request.method == "POST":
        index = request.form.get("index")
        connect = connectModel.get_connect(db_pool)
        messageModul.deleteMessage(connect["cursor"], index)
        connectModel.con_close(connect["con"])
        return redirect("/message")
    return redirect(url_for("member.member"))