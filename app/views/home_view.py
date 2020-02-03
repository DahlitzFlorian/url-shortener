from flask import render_template, Blueprint, request

from services import db
from services import shortener

blueprint = Blueprint("home", __name__, template_folder="templates")
DOMAIN = "https://fld.yt/s"


@blueprint.route("/home/", methods=["GET", "POST"])
@blueprint.route("/", methods=["GET", "POST"])
def home():
    context = {}

    if request.method == "POST":
        url = request.form.get("url")

        next_index = db.get_next_index()
        key = shortener.dehydrate(next_index)
        short_url = f"{DOMAIN}/{key}"

        db.add_link(short_url, url)

        context["short_url"] = short_url

    return render_template("index.html", **context)
