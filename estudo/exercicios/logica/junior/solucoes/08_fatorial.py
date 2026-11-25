"""Solucao de logica/junior/08_fatorial.py. Tente resolver o enunciado antes de abrir."""

def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError("n invalido")
    total = 1
    for i in range(2, n + 1):
        total *= i
    return total


if __name__ == "__main__":
    from _rodar import rodar

    rodar(fatorial=fatorial)
