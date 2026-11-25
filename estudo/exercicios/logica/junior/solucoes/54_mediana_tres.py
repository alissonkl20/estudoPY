"""Solucao de logica/junior/54_mediana_tres.py. Tente resolver o enunciado antes de abrir."""

def mediana_tres(a: int, b: int, c: int) -> int:
    return sorted((a, b, c))[1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(mediana_tres=mediana_tres)
