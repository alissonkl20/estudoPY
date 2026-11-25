"""Solucao de logica/junior/01_soma_pares.py. Tente resolver o enunciado antes de abrir."""

def soma_pares(nums: list[int]) -> int:
    return sum(n for n in nums if n % 2 == 0)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(soma_pares=soma_pares)
