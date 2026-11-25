"""Solucao de logica/pleno/13_caminhos_grade.py. Tente resolver o enunciado antes de abrir."""

def caminhos_grade(m: int, n: int) -> int:
    if m < 1 or n < 1:
        raise ValueError("grade invalida")
    linha = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            linha[c] += linha[c - 1]
    return linha[-1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(caminhos_grade=caminhos_grade)
