"""Solucao de logica/08_maior_soma.py. Tente resolver o enunciado antes de abrir."""


def maior_soma(nums: list[int], k: int) -> int:
    if k < 1 or k > len(nums):
        raise ValueError("janela invalida")
    atual = sum(nums[:k])
    melhor = atual
    for i in range(k, len(nums)):
        atual += nums[i] - nums[i - k]
        if atual > melhor:
            melhor = atual
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(maior_soma=maior_soma)
