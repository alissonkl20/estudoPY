"""Solucao de logica/junior/03_maior_numero.py. Tente resolver o enunciado antes de abrir."""

def maior_numero(nums: list[int]) -> int:
    if not nums:
        raise ValueError("lista vazia")
    return max(nums)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(maior_numero=maior_numero)
