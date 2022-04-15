"""
Testa cadastro de novo membro
"""
from src.http import HTTP_CREATED, HTTP_BAD_REQUEST


def test_post_member_success(client, mock_member, jwt_headers):
    """
    testa post member
    """
    data = {
        'name': mock_member['name'],
        'role': mock_member['role']
    }
    response = client.post('/members/', json=data, headers=jwt_headers)

    assert response.status_code == HTTP_CREATED


def test_post_member_fail_schema(client, jwt_headers):
    """
    testa falha por schema ao inserir novo membro
    """
    assert client.post('/members/', json={
        'name': 'test'
    }, headers=jwt_headers).status_code == HTTP_BAD_REQUEST

    assert client.post('/members/', json={
        'name': 'test',
        'role': 'test',
        'score_details': [{'points': 100, 'description': 'test'}]
    }, headers=jwt_headers).status_code == HTTP_BAD_REQUEST

    assert client.post('/members/', json={
        'name': None,
        'role': 'test'
    }, headers=jwt_headers).status_code == HTTP_BAD_REQUEST
