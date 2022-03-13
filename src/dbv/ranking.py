"""
Ranking dos desbravadores
"""
from flask import Blueprint
from src.utils import sort_by_index

ranking_bp = Blueprint('ranking_bp', __name__)


@ranking_bp.route('/api/ranking_dbv')
def get_ranking():
    """GET ranking dos dbvs baseado nos pontos
    """
    sort_by_index()
    return {}