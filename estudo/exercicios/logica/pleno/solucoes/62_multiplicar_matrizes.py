"""Solucao de logica/pleno/62_multiplicar_matrizes.py. Tente resolver o enunciado antes de abrir."""

def multiplicar_matrizes(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    if not a or not a[0] or not b or not b[0] or len(a[0]) != len(b):
        raise ValueError("matrizes incompativeis")
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(multiplicar_matrizes=multiplicar_matrizes)
