"""Solucao de logica/pleno/02_escadas.py. Tente resolver o enunciado antes de abrir."""

def escadas(n: int) -> int:
    if n < 1:
        raise ValueError("n invalido")
    if n <= 2:
        return n
    anterior, atual = 1, 2
    for _ in range(3, n + 1):
        anterior, atual = atual, anterior + atual
    return atual


if __name__ == "__main__":
    from _rodar import rodar

    rodar(escadas=escadas)
