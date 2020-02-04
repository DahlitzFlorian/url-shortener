import os

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
        shortener_password = os.environ.get("shortener_password")
        if not shortener_password or request.form.get("password") != shortener_password:
            context["short_url"] = "Wrong password"
            return render_template("index.html", **context)

        url = request.form.get("url")

        db_url = db.check_link_exist(url)
        if db_url is not None:
            context["short_url"] = db_url
            return render_template("index.html", **context)

        next_index = db.get_next_index()
        key = shortener.dehydrate(next_index)
        short_url = f"{DOMAIN}/{key}"

        db.add_link(short_url, url)

        context["short_url"] = short_url

    return render_template("index.html", **context)
