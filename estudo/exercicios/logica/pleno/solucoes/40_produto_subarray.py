"""Solucao de logica/pleno/40_produto_subarray.py. Tente resolver o enunciado antes de abrir."""

def produto_subarray(nums: list[int]) -> int:
    if not nums:
        raise ValueError("lista vazia")
    melhor = maior = menor = nums[0]
    for n in nums[1:]:
        candidatos = (n, maior * n, menor * n)
        maior = max(candidatos)
        menor = min(candidatos)
        melhor = max(melhor, maior)
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(produto_subarray=produto_subarray)
