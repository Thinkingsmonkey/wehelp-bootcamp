from flask import Blueprint, request, session, jsonify
from models.db_config import db_pool
import models.member_model as member_model
import models.connect_model as connect_model

api_controller = Blueprint("api", __name__)


@api_controller.route("/member", methods=["GET", "PATCH"])
def member_api():
    if request.method == "GET":
        falseReturn = jsonify({"data": None})
        if "username" not in session:
            return falseReturn, 401
        username = request.args.get("username")
        connect = connect_model.get_connect(db_pool)
        data = member_model.search_member(connect["cursor"], username)
        connect_model.con_close(connect["con"])
        if data == None:
            return falseReturn, 400
        return jsonify(
            {
                "data": {
                    "username": data[0],
                    "name": data[1],
                    "id": data[2],
                }
            }
        )

    if request.method == "PATCH":
        if "username" not in session:
            return jsonify({"error": True, "message": "更新失敗!"}), 401
        new_name = request.json.get("name")
        connect = connect_model.get_connect(db_pool)
        member_model.patch_name(connect["cursor"], session["id"], new_name)
        connect["con"].commit()
        data = member_model.search_member(connect["cursor"], session["username"])
        # 當 member 的 name 被修改後，session 也要一起修改
        connect_model.con_close(connect["con"])
        session["id"] = data[2]
        session["name"] = data[1]
        session["username"] = data[0]
        return jsonify(
            {
                "ok": True,
                "data": {
                    "username": data[0],
                    "name": data[1],
                },
            }
        )
