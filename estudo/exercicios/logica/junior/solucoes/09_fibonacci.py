"""Solucao de logica/junior/09_fibonacci.py. Tente resolver o enunciado antes de abrir."""

def fibonacci(n: int) -> int:
    if n < 1:
        raise ValueError("n invalido")
    anterior, atual = 1, 1
    for _ in range(n - 1):
        anterior, atual = atual, anterior + atual
    return anterior


if __name__ == "__main__":
    from _rodar import rodar

    rodar(fibonacci=fibonacci)
