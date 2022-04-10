"""
Testa rota que retorna apenas um membro baseado no id
"""
from bson.objectid import ObjectId
from src import database
from tests.conftest import MOCK_MEMBER_ID_STR
from src.http import HTTP_OK, HTTP_NOT_FOUND


def test_success_get_one_member(client, mock_member):
    """
    get member
    """
    database.insert_document('members', mock_member)
    response = client.get(f'/members/{MOCK_MEMBER_ID_STR}')

    assert response.status_code == HTTP_OK


def test_bad_request_get_one_member(client, mock_member):
    """
    Testa not found na rota get /member/<member_id>
    """
    response = client.get(f'members/{ObjectId()}')

    assert response.status_code == HTTP_NOT_FOUND
