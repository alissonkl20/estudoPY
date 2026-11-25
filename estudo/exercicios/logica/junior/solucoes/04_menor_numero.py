"""Solucao de logica/junior/04_menor_numero.py. Tente resolver o enunciado antes de abrir."""

def menor_numero(nums: list[int]) -> int:
    if not nums:
        raise ValueError("lista vazia")
    return min(nums)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(menor_numero=menor_numero)
