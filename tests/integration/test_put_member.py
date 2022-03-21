"""
Testa rota responsavel por atualizar dados dos membros
"""
from bson.objectid import ObjectId
from src import database
from tests.conftest import MOCK_MEMBER_ID
from src.http import HTTP_OK


def test_success_update_member(client, mock_member):
    """
    Testa atualizacao de dados dos membros e insercao de pontos
    """
    mock_member['_id'] = ObjectId(MOCK_MEMBER_ID)
    database.insert_document('members', mock_member)

    mock_score_details = [{'points': 100, 'description': 'description test'},
                          {'points': 200, 'description': 'description test'},
                          {'points': 300, 'description': 'description test'}]

    response = client.put(f'/members/{MOCK_MEMBER_ID}',
                          json={'score_details': mock_score_details,
                                'role': 'lider', 'name': 'joao'})

    member = database.fetch('members', {'_id': mock_member['_id']})[0]
    assert member['role'] == 'lider'
    assert member['name'] == 'joao'
    assert member['score'] == 600
    assert len(member['score_details']) == 3
    assert response.status_code == HTTP_OK
