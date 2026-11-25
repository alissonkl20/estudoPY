"""Solucao de logica/junior/42_rotacionar_direita.py. Tente resolver o enunciado antes de abrir."""

def rotacionar_direita(nums: list[int], k: int) -> list[int]:
    if k < 0:
        raise ValueError("k invalido")
    if not nums:
        return []
    k %= len(nums)
    if k == 0:
        return list(nums)
    return nums[-k:] + nums[:-k]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(rotacionar_direita=rotacionar_direita)
