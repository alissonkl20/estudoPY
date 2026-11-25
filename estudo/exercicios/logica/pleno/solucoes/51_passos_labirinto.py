"""Solucao de logica/pleno/51_passos_labirinto.py. Tente resolver o enunciado antes de abrir."""

def passos_labirinto(grade: list[list[int]], inicio: tuple[int, int], fim: tuple[int, int]) -> int:
    if not grade or not grade[0]:
        return -1
    linhas, colunas = len(grade), len(grade[0])

    def livre(r: int, c: int) -> bool:
        return 0 <= r < linhas and 0 <= c < colunas and grade[r][c] == 1

    ir, ic = inicio
    if not livre(ir, ic) or not livre(*fim):
        return -1
    fila = [(ir, ic, 0)]
    vistos = {(ir, ic)}
    while fila:
        r, c, dist = fila.pop(0)
        if (r, c) == fim:
            return dist
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if livre(nr, nc) and (nr, nc) not in vistos:
                vistos.add((nr, nc))
                fila.append((nr, nc, dist + 1))
    return -1


if __name__ == "__main__":
    from _rodar import rodar

    rodar(passos_labirinto=passos_labirinto)
