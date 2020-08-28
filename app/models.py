from datetime import datetime
from .extensions import db
from werkzeug.security import generate_password_hash,check_password_hash

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    email = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    photos = db.relationship('Photo', back_populates = 'catagory')
    injection_mold_categorys = db.relationship('Injection_Mold_Category', back_populates = 'category')

class Injection_Mold_Category(db.Model):
    __tablename__ = 'injection_mold_category'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category =db.relationship('Category', back_populates = 'injection_mold_categorys')

class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(64))
    filename = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',back_populates = 'photos')