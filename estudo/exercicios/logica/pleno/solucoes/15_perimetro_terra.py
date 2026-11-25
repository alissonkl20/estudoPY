"""Solucao de logica/pleno/15_perimetro_terra.py. Tente resolver o enunciado antes de abrir."""

def perimetro_terra(grade: list[list[int]]) -> int:
    if not grade:
        return 0
    linhas, colunas = len(grade), len(grade[0])
    total = 0
    for r in range(linhas):
        for c in range(colunas):
            if grade[r][c] != 1:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < linhas and 0 <= nc < colunas and grade[nr][nc] == 1):
                    total += 1
    return total


if __name__ == "__main__":
    from _rodar import rodar

    rodar(perimetro_terra=perimetro_terra)
