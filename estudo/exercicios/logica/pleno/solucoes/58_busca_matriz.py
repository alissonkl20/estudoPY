"""Solucao de logica/pleno/58_busca_matriz.py. Tente resolver o enunciado antes de abrir."""

def busca_matriz(matriz: list[list[int]], alvo: int) -> bool:
    if not matriz or not matriz[0]:
        return False
    linhas, colunas = len(matriz), len(matriz[0])
    inicio, fim = 0, linhas * colunas - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor = matriz[meio // colunas][meio % colunas]
        if valor == alvo:
            return True
        if valor < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False


if __name__ == "__main__":
    from _rodar import rodar

    rodar(busca_matriz=busca_matriz)
