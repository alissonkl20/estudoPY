"""Solucao de logica/pleno/34_majoritario.py. Tente resolver o enunciado antes de abrir."""

def majoritario(nums: list[int]) -> int:
    if not nums:
        raise ValueError("lista vazia")
    candidato = nums[0]
    saldo = 0
    for n in nums:
        if saldo == 0:
            candidato = n
        saldo += 1 if n == candidato else -1
    if nums.count(candidato) * 2 <= len(nums):
        raise ValueError("sem maioria")
    return candidato


if __name__ == "__main__":
    from _rodar import rodar

    rodar(majoritario=majoritario)
