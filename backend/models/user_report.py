from flask import  Flask, request 
from models.dbconfig import db 



class UserReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    report_type = db.Column(db.String(50))
    report_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"UserReport(user_id={self.user_id}, report_type='{self.report_type}', report_time='{self.report_time}, description='{self.description}')"