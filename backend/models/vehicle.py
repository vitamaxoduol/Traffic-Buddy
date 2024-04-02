from flask import  Flask, request
from models.dbconfig import db 

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    license_plate = db.Column(db.String(20), unique=True, nullable=False)
    owner_name = db.Column(db.String(100))
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    verified = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Vehicle(registration_number='{self.registration_number}', owner_name='{self.owner_name}', model='{self.model}')"
