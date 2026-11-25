"""Solucao de logica/junior/18_esta_ordenado.py. Tente resolver o enunciado antes de abrir."""

def esta_ordenado(nums: list[int]) -> bool:
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(esta_ordenado=esta_ordenado)
