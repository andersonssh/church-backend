"""
Testa autenticacao da api
"""
from src.http import HTTP_UNAUTHORIZED
from test_put_member import PUT_MEMBER_ROUTE
from src import database


def test_put_members_unauthorized(client, mock_member, jwt_headers):
    """Testa put de membros com e sem permissoes"""
    database.insert_document('members', mock_member)

    assert client.put(PUT_MEMBER_ROUTE, json={'name': 'test'},
                      headers={'Authorization': 'Bearer xyz'}).status_code == HTTP_UNAUTHORIZED
    assert client.put(PUT_MEMBER_ROUTE, json={'name': 'test'}).status_code == HTTP_UNAUTHORIZED


def test_post_members_unauthorized(client, jwt_headers):
    """
    Testa post de membros com e sem permissoes
    """
    payload = {'name': 'test', 'role': 'test'}
    assert client.post('/members/',
                       headers={'Authorization': 'Bearer xyz'},
                       json=payload).status_code == HTTP_UNAUTHORIZED
    assert client.post('/members/',
                       headers={'Authorization': 'Bearerxyz'},
                       json=payload).status_code == HTTP_UNAUTHORIZED
    assert client.post('/members/',
                       json=payload).status_code == HTTP_UNAUTHORIZED





