from enum import unique

from sqlalchemy.orm import backref, defaultload
from flaskBlog import db
from datetime import datetime

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     userName = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(40), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
#     # posts = db.relationship('Post', backref='author', lazy=True)
#     def __repr__(self):
#         return f'User({self.userName}, {self.email})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    postedDate = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'Post({self.title}, {self.description})'        