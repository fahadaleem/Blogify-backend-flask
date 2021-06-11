from flaskBlog import app
from flask import json, render_template, jsonify, request
from flaskBlog import db
from flaskBlog.models import Post

db.create_all()


@app.route("/")
def home():
    return 'Server Started'

@app.route("/get-all-post", methods=['GET'])
def get_all_posts():
    all_posts = Post.query.all()
    json = {
        "total_posts" : f'{len(all_posts)}',
        "posts" : f'{all_posts}'
    }
    return jsonify(json)
    
 


