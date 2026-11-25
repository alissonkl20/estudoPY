"""Solucao de logica/pleno/19_mais_frequentes.py. Tente resolver o enunciado antes de abrir."""

def mais_frequentes(nums: list[int], k: int) -> list[int]:
    if k < 1:
        raise ValueError("k invalido")
    from collections import Counter
    ordenados = sorted(Counter(nums).items(), key=lambda item: (-item[1], item[0]))
    return [valor for valor, _ in ordenados[:k]]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(mais_frequentes=mais_frequentes)
