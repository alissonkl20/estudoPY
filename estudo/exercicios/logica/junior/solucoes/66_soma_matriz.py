"""Solucao de logica/junior/66_soma_matriz.py. Tente resolver o enunciado antes de abrir."""

def soma_matriz(matriz: list[list[int]]) -> int:
    if not matriz:
        return 0
    largura = len(matriz[0])
    total = 0
    for linha in matriz:
        if len(linha) != largura:
            raise ValueError("matriz irregular")
        total += sum(linha)
    return total


if __name__ == "__main__":
    from _rodar import rodar

    rodar(soma_matriz=soma_matriz)
