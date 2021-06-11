from flaskBlog import app
from flask import json, render_template, jsonify, request
from flaskBlog import db
from flaskBlog.models import Post

db.create_all()

def convert_json_to_list(x):
    return {
        "id":f'{x.id}',
        "title":f'{x.title}',
        "description":f'{x.description}',
        "posted_date":f'{x.postedDate}'
    }


@app.route("/")
def home():
    return 'Server Started'

@app.route("/get-all-post", methods=['GET'])
def get_all_posts():
    all_posts = Post.query.all()

    all_posts = list(map(convert_json_to_list, all_posts))


    json = {
        "total_posts" : f'{len(all_posts)}',
        "posts" : f'{all_posts}'
    }
    return jsonify(json)
    
 


