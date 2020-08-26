from datetime import datetime
from .extensions import db


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    email = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)

class Admin(db.Model):
    __tablename__ = 'admin'
    pass

class Category(db.Model):
    __tablename__ = 'category'
    pass