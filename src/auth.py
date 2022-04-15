"""
Modulo de autenticacao
"""
import os
import datetime
from types import FunctionType
from functools import wraps
import jwt
import bcrypt
from flask import request
from src.http import HTTP_UNAUTHORIZED


def requires_auth(func: FunctionType):
    """
    Autentica a requisicao pelo token do usuario
    """

    @wraps(func)
    def decorated(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return {'message': 'Authorization header is mandatory'}, HTTP_UNAUTHORIZED
        auth_split = request.headers.get('Authorization').split()
        if len(auth_split) != 2:
            return {'message': 'invalid format token, use: Bearer <token>'}, HTTP_UNAUTHORIZED

        _, token = auth_split
        try:
            jwt.decode(token, key=os.environ['SECRET_KEY'], algorithms=['HS256'])
        except:
            return {'message': 'invalid token'}, HTTP_UNAUTHORIZED

        return func(*args, **kwargs)

    return decorated


def generate_jwt_token(user_id: str) -> str:
    """
    Cria o token jwt

    Args:
        user_id: documento da colecao de usuarios

    Returns:
        str: token da API
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, key=os.environ['SECRET_KEY'], algorithm='HS256')


def encrypt_password(password: str) -> bytes:
    """
    Criptografa uma senha

    Args:
        password: senha

    Returns:
        str: senha encriptada
    """
    return bcrypt.hashpw(bytes(password, encoding='utf-8'), bcrypt.gensalt())


def check_password(password: str, hashed_password: bytes) -> bool:
    """
    Verifica se a senha hasheada corresponde a senha geradora

    Args:
       password: senha
       hashed_password: senha hasheada

    Returns:
         bool: True se a senha corresponder e Falso caso contrario
    """
    return bcrypt.checkpw(bytes(password, encoding='utf-8'), hashed_password)
