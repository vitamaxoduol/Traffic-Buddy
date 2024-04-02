from flask import  Flask, request 
from models.dbconfig import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(13), nullable=False)

    reports = db.relationship('UserReport', backref='user', lazy=True)
    owned_vehicles = db.relationship('Vehicle', backref='user', lazy=True)

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"

