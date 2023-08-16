from flask import *
from controllers.member import memberCtrlr
from controllers.error import errorCtrlr
from controllers.message import messageCtrlr
from controllers.api import apiCtrlr
from controllers.square import squareCtrlr

app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "secretKey aaa"

@app.route("/")
def home():
    return render_template("index.html")

app.register_blueprint(memberCtrlr, url_prefix="/member")
app.register_blueprint(errorCtrlr, url_prefix="/error")
app.register_blueprint(messageCtrlr, url_prefix="/message")
app.register_blueprint(apiCtrlr, url_prefix="/api")
app.register_blueprint(squareCtrlr, url_prefix="/square")

if __name__ == "__main__":
    app.run(port=3000, debug=True)