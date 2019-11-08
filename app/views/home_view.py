from pathlib import Path

from flask import render_template, Blueprint, request

from app.services import db
from app.services import shortener

blueprint = Blueprint("home", __name__, template_folder="templates")
DOMAIN = "https://fld.yt/s"
DB_PATH = Path(__file__).parent.parent.parent / "db.txt"


@blueprint.route("/home/", methods=["GET", "POST"])
@blueprint.route("/", methods=["GET", "POST"])
def home():
    context = {}

    if request.method == "POST":
        url = request.form.get("url")
        next_index = db.get_next_index(DB_PATH)
        key = shortener.dehydrate(next_index)
        db.add_link(DB_PATH, key, url)
        context["short_url"] = f"{DOMAIN}/{key}"

    return render_template("index.html", **context)
