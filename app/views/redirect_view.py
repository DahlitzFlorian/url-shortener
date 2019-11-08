from pathlib import Path

from flask import render_template, redirect, Blueprint

from app.services import db

blueprint = Blueprint("redirection_service", __name__, template_folder="templates")
DB_PATH = Path(__file__).parent.parent.parent / "db.txt"


@blueprint.route("/s/<path:key>")
def redirect_service(key: str):
    destination = db.get_link(DB_PATH, key)
    if destination is not None:
        return redirect(destination, code=302)
    else:
        return render_template("404.html")
