"""Solucao de logica/junior/62_numero_faltante.py. Tente resolver o enunciado antes de abrir."""

def numero_faltante(nums: list[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(numero_faltante=numero_faltante)
