"""
Testa GET members
"""
from src.http import HTTP_OK


def test_success_get_members(client):
    """
    test success get members
    """
    response = client.get('/members/')

    assert response.status_code == HTTP_OK
