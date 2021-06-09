from flaskBlog import app
from flask import json, render_template, jsonify


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template('about.html')    