from flask import Blueprint, render_template

square_controller = Blueprint("square", __name__)


@square_controller.route("/<num>", methods=["POST"])
def square(num):
    number = int(num)
    answer = number * number
    return render_template("square.html", answer=answer)
