"""Solucao de logica/junior/50_indices.py. Tente resolver o enunciado antes de abrir."""

def indices(nums: list, alvo) -> list[int]:
    return [i for i, n in enumerate(nums) if n == alvo]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(indices=indices)
