"""Solucao de logica/junior/30_collatz.py. Tente resolver o enunciado antes de abrir."""

def collatz(n: int) -> int:
    if n < 1:
        raise ValueError("n invalido")
    passos = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        passos += 1
    return passos


if __name__ == "__main__":
    from _rodar import rodar

    rodar(collatz=collatz)
