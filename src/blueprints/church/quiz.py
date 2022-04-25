from flask import Blueprint, request, jsonify, escape
from src.http import (HTTP_BAD_REQUEST,
                      HTTP_OK,
                      HTTP_CREATED,
                      validate_content,
                      MimeTypes)
from src import database
import os
import json

with open('src/schemas/quiz/ranking/post.json', 'r') as f:
    POST_QUIZ_RANKING_SCHEMA = json.load(f)
MAX_LIMIT_QUESTIONS = 15

quiz_bp = Blueprint('quiz_bp', __name__)


def _get_quiz_questions(level=0, matter='all', limit=10) -> list:
    query = {}
    if level != 0:
        query['level'] = level
    if matter != 'all':
        query['matter'] = 'matter'

    return list(database.db.get_collection('quiz').aggregate([{'$match': query},
                                                              {'$addFields': {'n_random': {'$rand': {}}}},
                                                              {'$sort': {'n_random': 1}},
                                                              {'$unset': ['_id', 'n_random', 'created_at',
                                                                          'updated_at']},
                                                              {'$limit': limit}]))


def _get_questions_by_mode(mode: str, level, matter, limit) -> list:
    questions = []
    if mode == 'rank':
        for i in range(1, 4):
            questions += _get_quiz_questions(i)

    return questions


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

    return jsonify(_get_questions_by_mode('rank', level, matter, limit)), HTTP_OK


@quiz_bp.route('/quiz/ranking')
def ranking():
    result = database.db.get_collection('quiz_ranking').aggregate([
        {'$sort': {'score': -1}},
        {'$unset': ['_id', 'n_random', 'created_at', 'updated_at']},
        {'$limit': 15}
    ])
    return jsonify(list(result))


@quiz_bp.route('/quiz/ranking', methods=['POST'])
@validate_content(POST_QUIZ_RANKING_SCHEMA, MimeTypes.JSON)
def post_ranking():
    payload = request.json
    if os.getenv('QUIZ_PASS', '') == payload.get('pass', None):
        quiz_users = database.fetch('quiz_ranking',
                                    {'session_id': payload['session_id'],
                                     'name': payload['name'].strip()})

        if quiz_users:
            quiz_user = quiz_users[0]
            if payload['score'] > quiz_user['score']:
                database.db.get_collection('quiz_ranking').update_one(
                    {'session_id': payload['session_id']},
                    {'$set': {
                        'score': payload['score'],
                        'name': str(escape(payload['name']))}})
        else:
            database.insert_document('quiz_ranking',
                                     {
                                         'score': int(payload['score']),
                                         'name': str(escape(payload['name'])),
                                         'session_id': payload['session_id']
                                     })

    # SEMPRE RETORNA STATUS CODE DE SUCESSO!!!!!!!!!!!!!!!!!
    return {}, HTTP_CREATED
