from flask import Flask

app = Flask(__name__)

from views import home_view
from views import redirect_view

app.register_blueprint(home_view.blueprint)
app.register_blueprint(redirect_view.blueprint)

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, debug=True)
