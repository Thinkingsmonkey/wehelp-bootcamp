from flask import Blueprint, request, session, redirect, url_for, jsonify
from models.db_config import db_pool
import models.message_model as message_model
import models.connect_model as connect_model


message_controller = Blueprint("message", __name__)

#! 這裡為了實現 PRG 的模式，並沒有符合 RESTful API，在新增 api 中包含了 GET 方法
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


@message_controller.route("/<id>", methods=["DELETE"])
def delete_message(id):
    connect = connect_model.get_connect(db_pool)
    result = message_model.delete_message(connect["cursor"], id)
    connect_model.connect_close(connect["con"])
    if result:
        return jsonify({"message": "Delete successful"}), 200
    return jsonify({"message": "Delete failed"}), 404

