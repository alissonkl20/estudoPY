"""Solucao de logica/pleno/17_espiral.py. Tente resolver o enunciado antes de abrir."""

def espiral(matriz: list[list[int]]) -> list[int]:
    if not matriz or not matriz[0]:
        return []
    topo, baixo = 0, len(matriz) - 1
    esquerda, direita = 0, len(matriz[0]) - 1
    saida = []
    while topo <= baixo and esquerda <= direita:
        for c in range(esquerda, direita + 1):
            saida.append(matriz[topo][c])
        topo += 1
        for r in range(topo, baixo + 1):
            saida.append(matriz[r][direita])
        direita -= 1
        if topo <= baixo:
            for c in range(direita, esquerda - 1, -1):
                saida.append(matriz[baixo][c])
            baixo -= 1
        if esquerda <= direita:
            for r in range(baixo, topo - 1, -1):
                saida.append(matriz[r][esquerda])
            esquerda += 1
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(espiral=espiral)
