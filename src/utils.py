"""
Arquivo com funcoes variadas
"""

def sort_by_index(array: list, index: int = 0, reverse: bool = False) -> list:
    """Ordena lista de listas baseado no indice

    Args:
        array: lista com listas
        index: inteiro com o número do indice
        reverse: True faz a ordem inversa

    Raises:
        TypeError: Caso os elementos no indice
        selecionados não sejam do mesmo tipo
        IndexError: Caso algum elemento da lista não possua o indice informado

    Returns:
         None: Caso o indice não exista
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


