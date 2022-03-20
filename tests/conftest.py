"""
Arquivo de configuracao dos testes
"""
from unittest import mock
import json
import pytest
from mongomock import Database, MongoClient
from api import app
from src import database


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
        yield json.load(member)
