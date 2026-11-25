"""Solucao de logica/pleno/56_pico.py. Tente resolver o enunciado antes de abrir."""

def pico(nums: list[int]) -> int:
    if not nums:
        raise ValueError("lista vazia")
    return max(range(len(nums)), key=lambda i: nums[i])


if __name__ == "__main__":
    from _rodar import rodar

    rodar(pico=pico)
