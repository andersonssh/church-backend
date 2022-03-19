"""
Arquivo com funcoes variadas
"""
from datetime import datetime


def sort_lists_by_index(array: list, index: int = 0, reverse: bool = False) -> list:
    """Ordena listas dentro de uma lista. A ordem será dada pelo
    valor que o indice aponta dentro de cada lista. Por exemplo: com index = 0
    a função irá ordenar as listas de acordo com o valor que existe no indice 0 de cada lista ->
    [[indice0, indice1], [indice0, indice1]]

    Args:
        array: lista com listas
        index: inteiro com o número do indice
        reverse: True organiza em ordem decrescente

    Raises:
        TypeError: Caso os elementos no indice
        selecionado não sejam do mesmo tipo
        IndexError: Caso algum elemento da lista não possua o indice informado

    Returns:
         list: Lista organizada
    """
    for _ in range(len(array)):
        stop = True
        for i in range(len(array) - 1):
            if array[i][index] > array[i + 1][index]:
                stop = False
                array[i], array[i + 1] = array[i + 1], array[i]
        if stop:
            break

    return array[::-1] if reverse else array


def isodatetime():
    """
    Retorna a data atual formatada de acordo com o padrao
    internacional ISO 8601 sem microsegundos
    """
    return datetime.today().isoformat(' ', 'seconds')
