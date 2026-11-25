"""Solucao de logica/pleno/50_provincias.py. Tente resolver o enunciado antes de abrir."""

def provincias(n: int, estradas: list[list[int]]) -> int:
    if n < 1:
        raise ValueError("n invalido")
    pai = list(range(n))

    def achar(x: int) -> int:
        while pai[x] != x:
            pai[x] = pai[pai[x]]
            x = pai[x]
        return x

    for u, v in estradas:
        ru, rv = achar(u), achar(v)
        if ru != rv:
            pai[ru] = rv
    return len({achar(i) for i in range(n)})


if __name__ == "__main__":
    from _rodar import rodar

    rodar(provincias=provincias)
