import json
from flaskBlog import app
from flask import render_template, jsonify, request
from flaskBlog import db
from flaskBlog.models import Post

db.create_all()


def convert_json_to_list(x):
    return {
        "id": f'{x.id}',
        "title": f'{x.title}',
        "description": f'{x.description}',
        "posted_date": f'{x.postedDate}'
    }


@app.route("/")
def home():
    blog_post = Post.query.get(1)
    return render_template("index.html", json=convert_json_to_list(blog_post))


@app.route("/get-all-posts", methods=['GET'])
def get_all_posts():
    all_posts = Post.query.all()

    all_posts = list(map(convert_json_to_list, all_posts))

    json = {"total_posts": f'{len(all_posts)}', "posts": f'{all_posts}'}
    return jsonify(json)


@app.route("/add-new-post", methods=['POST'])
def add_new_post():
    title = request.json['title']
    description = request.json['description']
    new_post = Post(title=title, description=description)
    db.session.add(new_post)
    db.session.commit()
    return {"message": 'data added successfully!', "code": "200"}


@app.route("/post/<id>", methods=['GET'])
def get_post(id):
    blog_post = Post.query.get(id)
    if not blog_post:
        return {"message": "No Post Found", "code": "201"}
    else:
        return convert_json_to_list(blog_post)