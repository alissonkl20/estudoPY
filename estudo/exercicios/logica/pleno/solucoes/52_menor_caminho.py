"""Solucao de logica/pleno/52_menor_caminho.py. Tente resolver o enunciado antes de abrir."""

def menor_caminho(grafo: dict, origem: str, destino: str) -> int:
    import heapq
    if origem == destino:
        return 0
    fila = [(0, origem)]
    vistos = set()
    while fila:
        dist, no = heapq.heappop(fila)
        if no in vistos:
            continue
        vistos.add(no)
        if no == destino:
            return dist
        for vizinho, peso in grafo.get(no, []):
            if vizinho not in vistos:
                heapq.heappush(fila, (dist + peso, vizinho))
    return -1


if __name__ == "__main__":
    from _rodar import rodar

    rodar(menor_caminho=menor_caminho)
