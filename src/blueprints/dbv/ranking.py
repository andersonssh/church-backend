"""
Ranking dos desbravadores
"""
from flask import Blueprint, jsonify
from src.utils import sort_lists_by_index
from src.database import fetch
from src.http import HTTP_OK

ranking_bp = Blueprint('ranking_bp', __name__)


@ranking_bp.route('/ranking')
def get_ranking():
    """GET /ranking : ranking dos dbvs baseado nos pontos
    """
    members = fetch('members')

    data = [(member['name'], member['score'], member['score_details']) for member in members]

    ranked_by_points = sort_lists_by_index(data, index=1, reverse=True)

    return jsonify(ranked_by_points), HTTP_OK
