"""Solucao de logica/pleno/01_maior_soma_contigua.py. Tente resolver o enunciado antes de abrir."""

def maior_soma_contigua(nums: list[int]) -> int:
    if not nums:
        raise ValueError("lista vazia")
    melhor = atual = nums[0]
    for n in nums[1:]:
        atual = n if atual + n < n else atual + n
        if atual > melhor:
            melhor = atual
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(maior_soma_contigua=maior_soma_contigua)
