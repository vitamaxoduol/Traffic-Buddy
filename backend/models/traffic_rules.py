from models.dbconfig import db 

class TrafficRules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    region = db.Column(db.String(50), nullable=False)



    def __repr__(self):
        return f"UserReport(rule={self.rule}, description='{self.description}', region='{self.region}')"