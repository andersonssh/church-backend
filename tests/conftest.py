"""
Arquivo de configuracao dos testes
"""
import json
import os
from unittest import mock
import pytest
import jwt
from bson.objectid import ObjectId
from mongomock import Database, MongoClient
from api import app
from src import database

MOCK_MEMBER_ID_OBJECT_ID = ObjectId()
MOCK_MEMBER_ID_STR = str(MOCK_MEMBER_ID_OBJECT_ID)
MOCK_SCORE_DETAILS = [{'points': 100, 'description': 'description test'},
                      {'points': 200, 'description': 'description test'},
                      {'points': 300, 'description': 'description test'}]


@pytest.fixture
def client():
    """
    Injecao do test_client da api para os testes consumirem
    """
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def path_mongo_client():
    """
    Injecao do mock database
    """
    mock_db = Database(MongoClient(), '', _store=None)
    with mock.patch.object(database, 'db', mock_db):
        yield


@pytest.fixture
def mock_member():
    """
    mock member
    """
    with open('tests/mock/member.json', 'r', encoding='UTF-8') as member:
        member = json.load(member)
        member['_id'] = MOCK_MEMBER_ID_OBJECT_ID
        yield member


@pytest.fixture
def jwt_headers():
    """
    token para autenticacao de rotas
    """
    token = jwt.encode({'test': 'test'}, key=os.environ['SECRET_KEY'], algorithm='HS256')
    yield {'Authorization': f'Bearer {token}'}
