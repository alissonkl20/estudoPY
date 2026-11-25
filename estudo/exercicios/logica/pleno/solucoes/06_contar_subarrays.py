"""Solucao de logica/pleno/06_contar_subarrays.py. Tente resolver o enunciado antes de abrir."""

def contar_subarrays(nums: list[int], k: int) -> int:
    from collections import Counter
    vistos = Counter({0: 1})
    total = soma = 0
    for n in nums:
        soma += n
        total += vistos[soma - k]
        vistos[soma] += 1
    return total


if __name__ == "__main__":
    from _rodar import rodar

    rodar(contar_subarrays=contar_subarrays)
