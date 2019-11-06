from flask import render_template, Blueprint

blueprint = Blueprint("home", __name__, template_folder="templates")


@blueprint.route("/home/")
@blueprint.route("/")
def home():
    return render_template("index.html")
