"""Solucao de logica/pleno/46_proximo_maior.py. Tente resolver o enunciado antes de abrir."""

def proximo_maior(nums: list[int]) -> list[int]:
    saida = [-1] * len(nums)
    pilha = []
    for i, n in enumerate(nums):
        while pilha and nums[pilha[-1]] < n:
            saida[pilha.pop()] = n
        pilha.append(i)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(proximo_maior=proximo_maior)
