from flask import Flask
# from flask_jwt_extended import  JWTManager
from flask_migrate import Migrate
from models.dbconfig import db
from config import Config


app = Flask(__name__)

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traffic_buddy.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SECRET_KEY"]="f5109b3b6fb6671d477caa1c"
migrate=Migrate(app,db)
db.init_app(app)
# jwt = JWTManager(app)