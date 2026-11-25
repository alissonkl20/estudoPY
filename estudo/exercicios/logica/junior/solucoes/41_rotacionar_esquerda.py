"""Solucao de logica/junior/41_rotacionar_esquerda.py. Tente resolver o enunciado antes de abrir."""

def rotacionar_esquerda(nums: list[int], k: int) -> list[int]:
    if k < 0:
        raise ValueError("k invalido")
    if not nums:
        return []
    k %= len(nums)
    return nums[k:] + nums[:k]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(rotacionar_esquerda=rotacionar_esquerda)
