from flask import Blueprint, render_template

square_controller = Blueprint("square", __name__)


@square_controller.route("/<int:number>", methods=["POST"])
def square(number):
    answer = number * number
    return render_template("square.html", answer=answer)
