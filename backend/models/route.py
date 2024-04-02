from models.dbconfig import db 

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    traffic_level = db.Column(db.Integer, nullable=False)
    recommended = db.Column(db.Boolean, default=False)



    def __repr__(self):
        return f"Route(origin='{self.origin}', destination='{self.destination}', distance={self.distance}, duration={self.duration}, traffic_level={self.traffic_level}, recommended={self.recommended})"