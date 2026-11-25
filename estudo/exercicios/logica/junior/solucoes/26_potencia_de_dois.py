"""Solucao de logica/junior/26_potencia_de_dois.py. Tente resolver o enunciado antes de abrir."""

def potencia_de_dois(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0


if __name__ == "__main__":
    from _rodar import rodar

    rodar(potencia_de_dois=potencia_de_dois)
