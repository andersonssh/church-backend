"""
Testes da rota GET de ranking
"""
from src.http import HTTP_OK
from src import database


def test_success_ranking_get(client, mock_member):
    """
    test de sucesso para a rota /ranking
    """
    mock_member['_id'] = '1'
    database.insert_document('members', mock_member)
    mock_member['_id'] = '2'
    database.insert_document('members', mock_member)
    mock_member['_id'] = '3'
    database.insert_document('members', mock_member)
    mock_member['_id'] = '4'
    database.insert_document('members', mock_member)

    response = client.get('/ranking')
    assert response.status_code == HTTP_OK
    assert len(response.json) == 4
