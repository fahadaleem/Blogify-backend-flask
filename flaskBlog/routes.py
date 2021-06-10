from flaskBlog import app
from flask import json, render_template, jsonify, request
from flaskBlog import db
from flaskBlog.models import User


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template('about.html')    


@app.route("/get-all-users", methods=["GET"])
def get_all_users():
    users = User.query.all() 
    return {
        "users":f'{users[0].userName}'
    }    


@app.route("/post-new-data", methods=["POST"])
def post_data():
    print(User.query.all())
    return 'data accepted'

