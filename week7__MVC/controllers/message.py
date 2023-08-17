from flask import Blueprint, request, session, redirect, url_for
from models.db_config import db_pool
import models.message_model as message_model
import models.connect_model as connect_model


message_controller = Blueprint("message", __name__)


@message_controller.route("/", methods=["POST", "GET"])
def create_message():
    if request.method == "POST":
        content = request.form.get("content")
        # 操控數據庫 添加留言
        data = {
            "id": session["id"],
            "username": session["username"],
            "name": session["name"],
            "content": content,
        }
        connect = connect_model.get_connect(db_pool)
        message_model.create_message(connect["cursor"], data)
        connect_model.connect_close(connect["con"])
        return redirect("/message")
    return redirect(url_for("member.member"))


@message_controller.route("/del", methods=["POST", "GET"])
def delete_message():
    if request.method == "POST":
        index = request.form.get("index")
        connect = connect_model.get_connect(db_pool)
        message_model.delete_message(connect["cursor"], index)
        connect_model.connect_close(connect["con"])
        return redirect("/message")
    return redirect(url_for("member.member"))
