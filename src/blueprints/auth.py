import requests
from flask import Blueprint, request
from src import database, auth
from src.http import HTTP_UNAUTHORIZED

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    """Login"""
    payload = request.json
    username = payload['username']
    password = payload['password']

    users = database.fetch('users', {'username': username})
    if not users:
        return {}, HTTP_UNAUTHORIZED

    user = users[0]
    hashed_password = user['password']
    if not auth.check_password(password, hashed_password):
        return {}, HTTP_UNAUTHORIZED

    token = auth.generate_jwt_token(str(user['_id']))
    return {
        'token': token,
        'user': {'username': user['username']},
    }
