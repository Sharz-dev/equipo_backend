from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"msg": "Invalid JSON payload"}), 400

        email = data["email"]
        password = data["password"]

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({"msg": "Invalid email or password"}), 401

        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token)

    except KeyError as ke:
        return jsonify({"msg": f"Missing required field: {str(ke)}"}), 400

    except AttributeError:
        return jsonify({"msg": "Invalid request structure or user model error"}), 500

    except Exception as e:
        return jsonify({"msg": "An unexpected error occurred", "error": str(e)}), 500
