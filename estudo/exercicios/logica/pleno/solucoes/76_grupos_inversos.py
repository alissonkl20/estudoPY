"""Solucao de logica/pleno/76_grupos_inversos.py. Tente resolver o enunciado antes de abrir."""

def grupos_inversos(nums: list[int], k: int) -> list[int]:
    if k < 1:
        raise ValueError("k invalido")
    saida = list(nums)
    for i in range(0, len(saida), k):
        if i + k <= len(saida):
            saida[i : i + k] = reversed(saida[i : i + k])
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(grupos_inversos=grupos_inversos)
