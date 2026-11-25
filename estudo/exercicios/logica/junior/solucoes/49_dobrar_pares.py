"""Solucao de logica/junior/49_dobrar_pares.py. Tente resolver o enunciado antes de abrir."""

def dobrar_pares(nums: list[int]) -> list[int]:
    return [n * 2 if n % 2 == 0 else n for n in nums]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(dobrar_pares=dobrar_pares)
