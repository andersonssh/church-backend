"""
Ranking dos desbravadores
"""
from flask import Blueprint
from src.utils import sort_by_index
from src.database import fetch
from src.http import HTTP_OK

ranking_bp = Blueprint('ranking_bp', __name__, url_prefix='/ranking')


@ranking_bp.route('/')
def get_ranking():
    """GET /ranking : ranking dos dbvs baseado nos pontos
    """
    members = fetch('members')

    data = [
        [member['name'], member['points']] for member in members
    ]

    ranked_by_points = sort_by_index(data, index=1, reverse=True)

    return {'data': ranked_by_points}, HTTP_OK
