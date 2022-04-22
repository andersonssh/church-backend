from flask import Blueprint, request, jsonify
from src.http import HTTP_BAD_REQUEST, HTTP_OK
from src import database

MAX_LIMIT_QUESTIONS = 15

quiz_bp = Blueprint('quiz_bp', __name__)


def _get_quiz_questions(level=0, matter='all', limit=10):
    query = {}
    if level != 0:
        query['level'] = level
    if matter != 'all':
        query['matter'] = 'matter'

    match = {'$match': query}
    return database.db.get_collection('quiz').aggregate([match,
                                                         {'$addFields': {'n_random': {'$rand': {}}}},
                                                         {'$sort': {'n_random': 1}},
                                                         {'$unset': ['_id', 'n_random', 'created_at', 'updated_at']},
                                                         {'$limit': limit}])


@quiz_bp.route('/quiz')
def quiz():
    level = request.args.get('level', '0')
    matter = request.args.get('matter', 'all')
    limit = request.args.get('limit', '10')
    level_max = 3
    matter_alloweds = ['all']

    if level.isnumeric() and 0 <= int(level) <= level_max:
        level = int(level)
    else:
        return {'message': f'level deve ser um numero entre 0 e {level_max}'}, HTTP_BAD_REQUEST

    if matter not in matter_alloweds:
        return {'message': f'Materias permitidas: {matter_alloweds}'}, HTTP_BAD_REQUEST

    if limit.isnumeric() and 0 <= int(limit) <= MAX_LIMIT_QUESTIONS:
        limit = int(limit)
    else:
        return {'message': f'Limite max: {MAX_LIMIT_QUESTIONS}'}, HTTP_BAD_REQUEST

    return jsonify(list(_get_quiz_questions(level, matter, limit))), HTTP_OK
