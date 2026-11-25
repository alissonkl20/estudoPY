"""Solucao de logica/pleno/78_k_menores.py. Tente resolver o enunciado antes de abrir."""

def k_menores(nums: list[int], k: int) -> list[int]:
    if k < 1:
        raise ValueError("k invalido")
    return sorted(set(nums))[:k]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(k_menores=k_menores)
