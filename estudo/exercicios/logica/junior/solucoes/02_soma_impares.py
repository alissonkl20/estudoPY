"""Solucao de logica/junior/02_soma_impares.py. Tente resolver o enunciado antes de abrir."""

def soma_impares(nums: list[int]) -> int:
    return sum(n for n in nums if n % 2 != 0)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(soma_impares=soma_impares)
