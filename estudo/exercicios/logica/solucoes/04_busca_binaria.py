"""Solucao de logica/04_busca_binaria.py. Tente resolver o enunciado antes de abrir."""


def indice(lista: list[int], alvo: int) -> int:
    inicio = 0
    fim = len(lista) - 1
    achou = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            achou = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return achou


if __name__ == "__main__":
    from _rodar import rodar

    rodar(indice=indice)
