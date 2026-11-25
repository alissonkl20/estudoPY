"""Solucao de logica/pleno/61_crivo.py. Tente resolver o enunciado antes de abrir."""

def crivo(n: int) -> list[int]:
    if n < 2:
        return []
    marcado = [True] * (n + 1)
    marcado[0] = marcado[1] = False
    p = 2
    while p * p <= n:
        if marcado[p]:
            for m in range(p * p, n + 1, p):
                marcado[m] = False
        p += 1
    return [i for i, ok in enumerate(marcado) if ok]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(crivo=crivo)
