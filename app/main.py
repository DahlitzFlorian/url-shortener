from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, debug=True)
