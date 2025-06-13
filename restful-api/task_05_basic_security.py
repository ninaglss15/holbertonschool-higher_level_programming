#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

from flask_httpauth import HTTPBasicAuth

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "ma_cle_secrete"

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Provides a basic authentication message.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=["POST"])
def post_login():
    """
    Handle user login and return an access token.
    """
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Bad Request"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Bad Request"}), 400

    user = users.get(username)
    if user is None or not check_password_hash(user["password"], password):
        return jsonify({"error": "Unauthorized"}), 401

    token = create_access_token(identity=username)
    return jsonify(access_token=token), 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Function to simulate JWT (JSON Web Token) protected access.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Checks if the current user has admin privileges.
    """
    user = get_jwt_identity()
    if users[user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


if __name__ == "__main__":
    app.run()
