from flask import Blueprint, render_template
squareCtrlr = Blueprint("square", __name__)

@squareCtrlr.route("/<num>", methods=["POST"])
def square(num):
    number = int(num)
    answer = number * number
    return render_template("square.html", answer=answer)
