"""
Testa rota responsavel por atualizar dados dos membros
"""
from src import database
from tests.conftest import MOCK_MEMBER_ID_STR, MOCK_MEMBER_ID_OBJECT_ID, MOCK_SCORE_DETAILS
from src.http import HTTP_OK, HTTP_BAD_REQUEST

PUT_MEMBER_ROUTE = '/members/' + MOCK_MEMBER_ID_STR


def test_update_member_success(client, mock_member):
    """
    Testa atualizacao de dados dos membros e insercao de pontos
    """
    database.insert_document('members', mock_member)

    response_test1 = client.put(PUT_MEMBER_ROUTE,
                          json={'score_details': MOCK_SCORE_DETAILS,
                                'role': 'lider', 'name': 'joao'})

    member_test1 = database.fetch('members', {'_id': MOCK_MEMBER_ID_OBJECT_ID})[0]

    assert len(member_test1['score_details']) == 3
    assert response_test1.status_code == HTTP_OK

    response_test2 = client.put(PUT_MEMBER_ROUTE,
                          json={'score_details': MOCK_SCORE_DETAILS})

    member_test2 = database.fetch('members', {'_id': MOCK_MEMBER_ID_OBJECT_ID})[0]

    assert member_test2['role'] == 'lider'
    assert member_test2['name'] == 'joao'
    assert member_test2['score'] == 1200
    assert len(member_test2['score_details']) == 6
    assert response_test2.status_code == HTTP_OK


def test_update_member_fail_schema(client, mock_member):
    """
    testa falha por schema ao atualizar membro
    """
    database.insert_document('members', mock_member)

    assert client.put(PUT_MEMBER_ROUTE, json={
        'score_details': [100, 'test']
    }).status_code == HTTP_BAD_REQUEST

    assert client.put(PUT_MEMBER_ROUTE, json={
        'score_details': [{'points': '100', 'description': 'test'}]
    }).status_code == HTTP_BAD_REQUEST

    assert client.put(PUT_MEMBER_ROUTE, json={
        'score': 1200
    }).status_code == HTTP_BAD_REQUEST
