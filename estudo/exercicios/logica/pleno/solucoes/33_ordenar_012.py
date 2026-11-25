"""Solucao de logica/pleno/33_ordenar_012.py. Tente resolver o enunciado antes de abrir."""

def ordenar_012(nums: list[int]) -> list[int]:
    return [0] * nums.count(0) + [1] * nums.count(1) + [2] * nums.count(2)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(ordenar_012=ordenar_012)
