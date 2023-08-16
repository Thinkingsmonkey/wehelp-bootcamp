from flask import Blueprint, request, session, redirect, url_for, jsonify
from model.dbConfig import db_pool
import model.memberModel as memberModel
import model.connectModel as connectModel

apiCtrlr = Blueprint("api", __name__)

@apiCtrlr.route("/member", methods=["GET", "PATCH"])
def memberAPI():
    if request.method == "GET":
        falseReturn = jsonify({"data":None})
        if "username" not in session:
            return falseReturn, 401
        username = request.args.get("username")
        connect = connectModel.get_connect(db_pool)
        data = memberModel.search_member(connect["cursor"], username)
        connectModel.con_close(connect["con"])
        if data == None:
            return falseReturn, 400
        return jsonify({ "data": {
            "username": data[0],
            "name": data[1],
            "id": data[2],
        }})
    
    if request.method == "PATCH":
        if "username" not in session:
            return jsonify({"error":True, "message": "更新失敗!"}), 401
        newName = request.json.get("name")
        connect = connectModel.get_connect(db_pool)
        memberModel.patch_name(connect["cursor"], session["id"], newName)
        connect["con"].commit()
        data = memberModel.search_member(connect["cursor"], session["username"])
        # 當 member 的 name 被修改後，session 也要一起修改
        connectModel.con_close(connect["con"])
        session["id"] = data[2]
        session["name"] = data[1]
        session["username"] = data[0]
        return jsonify({ 
            "ok": True,
            "data": {
            "username": data[0],
            "name": data[1],
            }
        })