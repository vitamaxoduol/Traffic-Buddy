from flask import request, jsonify, current_app
from functools import wraps
from datetime import timedelta, datetime
from models.user import User
# from models.dbconfig import db
from config import Config
from apis.authentication import authenticate_api, validate_token
# import jwt

def user_apis(app, db):
    @app.route("/api/users", methods=["GET"])
    @authenticate_api
    def get_users():
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    @app.route("/api/users/<int:user_id>", methods=["GET"])
    @authenticate_api
    def get_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return jsonify(user.to_dict())

    @app.route("/api/users/<int:user_id>/vehicles", methods=["GET"])
    @authenticate_api
    def get_user_vehicles(user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        vehicles = user.owned_vehicles
        return jsonify([vehicle.to_dict() for vehicle in vehicles])


    @app.route("/api/users/logout", methods=["POST"])
    def logout_user():
        data = request.get_json()

        # Validate user data
        if not data or "token" not in data:
            return {"error": "Invalid or missing authentication token"}, 400

        token = data.get("token")

        # Validate the token
        user = validate_token(token)
        if not user:
            return {"error": "Invalid or expired authentication token"}, 401

        # Invalidate the token
        user.password = None
        db.session.commit()

        return {"message": "Logged out successfully"}, 200