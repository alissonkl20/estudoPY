"""Solucao de logica/pleno/53_custo_mst.py. Tente resolver o enunciado antes de abrir."""

def custo_mst(n: int, arestas: list[tuple[int, int, int]]) -> int:
    if n < 1:
        raise ValueError("n invalido")
    pai = list(range(n))

    def achar(x: int) -> int:
        while pai[x] != x:
            pai[x] = pai[pai[x]]
            x = pai[x]
        return x

    custo = usados = 0
    for u, v, w in sorted(arestas, key=lambda aresta: aresta[2]):
        ru, rv = achar(u), achar(v)
        if ru != rv:
            pai[ru] = rv
            custo += w
            usados += 1
    if usados != n - 1:
        return -1
    return custo


if __name__ == "__main__":
    from _rodar import rodar

    rodar(custo_mst=custo_mst)
