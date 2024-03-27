# /app/api/user_api.py-1-A+
from flask import Blueprint, request, jsonify
from ..services.auth_service import AuthService
from ..models.user import User

user_api_blueprint = Blueprint('user_api', __name__)
auth_service = AuthService()

@user_api_blueprint.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration. Expects username, email, and password in the request data.
    """
    data = request.json
    if data is None:
        return jsonify({'error': 'No request data provided'}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 409

    user = auth_service.register_user(username, email, password)
    return jsonify({'message': 'User registered successfully', 'user_id': user.id}), 201


@user_api_blueprint.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login. Expects email and password in the request data.
    Returns a JWT if login is successful.
    """
    data = request.json
    if data is None:
        return jsonify({'error': 'No request data provided'}), 400

    email = data.get('email')
    password = data.get('password')

    if auth_service.authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        token = auth_service.generate_token(user.id)
        return jsonify({'message': 'Login successful', 'token': token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

