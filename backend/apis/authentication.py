from flask import request, current_app, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import timedelta, datetime, timezone
from models.user import User
from models.dbconfig import db
from config import Config
import jwt


def authenticate_api(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("x-api-key")
        if api_key != "Hr*ugf(N*&YH":
            return jsonify({"error": "Invalid or missing API authentication key"}), 401
        return func(*args, **kwargs)
    return wrapper

# Generate authentication token for a user
def generate_token(user_id):
    payload = {'user_id': user_id, 'exp': datetime.now(timezone.utc) + timedelta(days=1)}
    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm='HS256')
    return token

def validate_token(token):
    try:
        payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=['HS256'])
        return "user_id" in payload
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

def authentication_api(app, db):

    @app.route("/api/register", methods=["POST"])
    def register():
        data = request.get_json()

        # Validate user data
        if not data or "email" not in data or "password" not in data or "phone_number" not in data or "username" not in data:
            return jsonify({"error": "Invalid or missing user data"}), 400

        email = data.get("email")
        username =data.get("username")
        password = data.get("password")
        phone_number = data.get("phone_number")

        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "User already exists"}), 409
        
        # Check if the user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"error": "User with such a username already exists"}), 409

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Create a new user
        new_user = User(email=email, username=username, password=hashed_password, phone_number=phone_number)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    @app.route("/api/login", methods=["POST"])
    def login():
        data = request.get_json()

        # Validate user data
        if not data or "username" not in data or "password" not in data:
            return {"error": "Invalid or missing user data"}, 400

        username = data.get("username")
        password = data.get("password")

        # Check if the user exists
        user = User.query.filter_by(username=username).first()
        if not user:
            return {"error": "Invalid credentials"}, 401
            
        # Verify the password
        if not check_password_hash(user.password, password):
            return {"error": "Invalid credentials"}, 401

        # Generate an authentication token
        token = generate_token(user.id)

        return {"token": token}, 200

    @app.route("/api/protected", methods=["GET"])
    @authenticate_api
    def protected():
        # This endpoint is only accessible by authenticated users
        return {"message": "This is a protected resource"}, 200