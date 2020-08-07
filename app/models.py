from datetime import datetime
from . import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    email = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)