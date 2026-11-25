"""Solucao de logica/pleno/54_tem_ciclo.py. Tente resolver o enunciado antes de abrir."""

def tem_ciclo(n: int, arestas: list[tuple[int, int]]) -> bool:
    grafo = [[] for _ in range(n)]
    for u, v in arestas:
        grafo[u].append(v)
    cor = [0] * n

    def visitar(no: int) -> bool:
        cor[no] = 1
        for vizinho in grafo[no]:
            if cor[vizinho] == 1 or (cor[vizinho] == 0 and visitar(vizinho)):
                return True
        cor[no] = 2
        return False

    return any(cor[i] == 0 and visitar(i) for i in range(n))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(tem_ciclo=tem_ciclo)
