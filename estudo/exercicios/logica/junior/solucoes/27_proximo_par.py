"""Solucao de logica/junior/27_proximo_par.py. Tente resolver o enunciado antes de abrir."""

def proximo_par(n: int) -> int:
    if n % 2 == 0:
        return n
    return n + 1


if __name__ == "__main__":
    from _rodar import rodar

    rodar(proximo_par=proximo_par)
