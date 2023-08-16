from flask import *
from controllers.member import member_controller
from controllers.error import error_controller
from controllers.message import message_controller
from controllers.api import api_controller
from controllers.square import square_controller

app = Flask(__name__, static_folder="views/public", static_url_path="/")
app.secret_key = "secretKey aaa"
app.template_folder = "views/templates"


@app.route("/")
def home():
    return render_template("index.html")


app.register_blueprint(member_controller, url_prefix="/member")
app.register_blueprint(error_controller, url_prefix="/error")
app.register_blueprint(message_controller, url_prefix="/message")
app.register_blueprint(api_controller, url_prefix="/api")
app.register_blueprint(square_controller, url_prefix="/square")

if __name__ == "__main__":
    app.run(port=3000, debug=True)
