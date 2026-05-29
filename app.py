from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pages")
def pages():
    return render_template("pages.html")


@app.route("/topics")
def topics():
    return render_template("topics.html")


@app.route("/recent")
def recent():
    return render_template("recent.html")
