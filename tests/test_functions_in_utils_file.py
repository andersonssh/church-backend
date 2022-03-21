"""
testes unitarios
"""
from src.utils import sort_lists_by_index


def test_da_funcao_que_ordena_o_ranking():
    """
    test sort_lists_by_index
    """
    data = [('joao', 200), ('marcio', 300), ('jose', 100)]
    assert [('jose', 100), ('joao', 200), ('marcio', 300)] ==\
        sort_lists_by_index(data, index=1)
    assert [('marcio', 300), ('joao', 200), ('jose', 100)] ==\
        sort_lists_by_index(data, index=1, reverse=True)
