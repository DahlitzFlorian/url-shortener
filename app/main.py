from flask import Flask

from data.setup import setup_db

app = Flask(__name__)

from views import home_view
from views import redirect_view

app.register_blueprint(home_view.blueprint)
app.register_blueprint(redirect_view.blueprint)

setup_db()

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, debug=True)
