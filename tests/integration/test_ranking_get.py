"""
Testes da rota GET de ranking
"""
from src.http import HTTP_OK
from src import database


def test_success_ranking_get(client, mock_member):
    """
    test de sucesso para a rota /ranking
    """
    database.insert_document('members', mock_member)

    response = client.get('/ranking/')

    assert response.status_code == HTTP_OK
