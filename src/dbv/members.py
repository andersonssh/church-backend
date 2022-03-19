"""
Rotas para controle de dados dos membros do clube de dbv
"""
from flask import Blueprint, request, jsonify
from src.database import insert_document, fetch, set_document_by_id
from src.http import HTTP_CREATED, HTTP_OK, HTTP_NOT_FOUND
from bson.objectid import ObjectId


members_bp = Blueprint('members_bp', __name__, url_prefix='/members')


@members_bp.route('/', methods=['GET'])
def get_members():
    """Retorna todos os membros em uma lista de dicionarios.
    """
    members = fetch('members')

    data = []
    print(members)
    for member in members:
        member['_id'] = str(member['_id'])
        data.append(member)

    return jsonify(data), HTTP_OK


@members_bp.route('/', methods=['POST'])
def post_member():
    """Insere novo membro. O json da requisicao deve conter a chave
    "name" e "role"
    """
    payload = request.json

    name = payload['name']
    role = payload['role']

    response = insert_document('members', {'name': name,
                                           'role': role,})

    return {'document_id': response[0],
            'created_at': response[1]}, HTTP_CREATED


@members_bp.route('/<string:member_id>', methods=['PUT'])
def update_member(member_id):
    """
    Atualiza dados dos membros. Todos os campos são tem seus valores substituidos com exceção
    do campo points_details que é incrementado com novos valores

    Args:
        member_id (str): id do membro a ser editado
    """
    members = fetch('members', {'_id': ObjectId(member_id)})

    if not members:
        return {'error': 'member not found'}, HTTP_NOT_FOUND

    payload = request.json

    if 'score_details' in payload.keys():
        member = members[0]

        recorded_score = member['score']
        recorded_score_details = member['score_details']

        payload['score'] = sum([item[0] for item in recorded_score_details]) + recorded_score
        payload['score_details'] = payload['score_details'] + recorded_score_details

    updated_at = set_document_by_id('members', member_id, payload)

    return {'updated_at': updated_at}, HTTP_OK
