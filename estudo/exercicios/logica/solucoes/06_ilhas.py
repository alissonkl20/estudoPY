"""Solucao de logica/06_ilhas.py. Tente resolver o enunciado antes de abrir."""


def contar_ilhas(mapa: list[list[int]]) -> int:
    if not mapa or not mapa[0]:
        return 0
    linhas = len(mapa)
    colunas = len(mapa[0])
    visto = [[False] * colunas for _ in range(linhas)]

    def visitar(inicio_i: int, inicio_j: int) -> None:
        pilha = [(inicio_i, inicio_j)]
        visto[inicio_i][inicio_j] = True
        while pilha:
            i, j = pilha.pop()
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni = i + di
                nj = j + dj
                if (
                    0 <= ni < linhas
                    and 0 <= nj < colunas
                    and mapa[ni][nj] == 1
                    and not visto[ni][nj]
                ):
                    visto[ni][nj] = True
                    pilha.append((ni, nj))

    total = 0
    for i in range(linhas):
        for j in range(colunas):
            if mapa[i][j] == 1 and not visto[i][j]:
                visitar(i, j)
                total += 1
    return total


if __name__ == "__main__":
    from _rodar import rodar

    rodar(contar_ilhas=contar_ilhas)
