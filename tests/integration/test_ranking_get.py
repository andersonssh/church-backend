"""
Testes da rota GET de ranking
"""
from src.http import HTTP_OK


def test_success_ranking_get(client):
    """
    test de sucesso para a rota /ranking
    """
    response = client.get('/members/')

    assert response.status_code == HTTP_OK
