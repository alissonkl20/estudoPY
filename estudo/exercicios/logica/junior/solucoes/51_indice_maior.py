"""Solucao de logica/junior/51_indice_maior.py. Tente resolver o enunciado antes de abrir."""

def indice_maior(nums: list[int]) -> int:
    if not nums:
        raise ValueError("lista vazia")
    melhor = 0
    for i, n in enumerate(nums):
        if n > nums[melhor]:
            melhor = i
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(indice_maior=indice_maior)
