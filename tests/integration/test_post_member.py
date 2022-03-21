"""
Testa cadastro de novo membro
"""
from src.http import HTTP_CREATED


def test_success_post_member(client, mock_member):
    """
    testa post member
    """
    data = {
        'name': mock_member['name'],
        'role': mock_member['role']
    }
    response = client.post('/members/', json=data)

    assert response.status_code == HTTP_CREATED
