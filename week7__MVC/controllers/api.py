from flask import Blueprint, request, session, jsonify
from models.db_config import db_pool
import models.member_model as member_model
import models.connect_model as connect_model

api_controller = Blueprint("api", __name__)

#! 修改為符合 RESTful API 規格：
# 1. 狀態碼 401 與 403 差別，401(未驗證，提示進行身分驗證)、403(已驗證但不具備訪問權限)，所以 "username" not in session 成立時是 401
# 2. 當資源不存在時，使用 404，例如：找不到該 username，data == None 時
@api_controller.route("/member", methods=["GET", "PATCH"])
def member_api():
    if request.method == "GET":
        falseReturn = jsonify({"data": None})
        if "username" not in session:
            return falseReturn, 401
        username = request.args.get("username")
        connect = connect_model.get_connect(db_pool)
        data = member_model.search_member(connect["cursor"], username)
        connect_model.connect_close(connect["con"])
        if data == None:
            return falseReturn, 404
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
        connect_model.connect_close(connect["con"])
        username_db, name_db, id_db = data
        # 當 member 的 name 被修改後，session 也要一起修改
        session["id"] = id_db
        session["name"] = name_db
        session["username"] = username_db
        return jsonify(
            {
                "ok": True,
                "data": {
                    "username": data[0],
                    "name": data[1],
                },
            }
        )
