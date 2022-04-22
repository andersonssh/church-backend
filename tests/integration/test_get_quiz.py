"""testes do quiz"""
from src import database
import json

with open('tests/mock/quiz.json') as f:
    MOCK_QUESTIONS_QUIZ = json.load(f)


# APARENTEMENTE MONGOMOCK NAO DA SUPORTE

# def test_quiz_filters_success(client):
#     """Teste sucesso quiz"""
#     database.db.get_collection('quiz').insert_many(MOCK_QUESTIONS_QUIZ)
#
#     all_matter_all_levels = client.get('/quiz?limit=15').json
#     # all_matter_all_levels_limit_3 = client.get('/quiz?limit=3').json
#     # all_matter_only_level1 = client.get('/quiz?level=1').json
#     # only_matter_jesus_only_level_1 = client.get('/quiz?matter=jesus&level=1').json
#     # only_matter_ceation_of_the_world_only_level_3 = client.\
#     #     get('/quiz?matter=creation_of_the_world&level=2').json
#
#     assert len(all_matter_all_levels) == 12
#
#     assert 1==2
