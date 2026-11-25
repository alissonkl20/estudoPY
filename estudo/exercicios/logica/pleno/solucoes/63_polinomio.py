"""Solucao de logica/pleno/63_polinomio.py. Tente resolver o enunciado antes de abrir."""

def polinomio(coefs: list[int], x: int) -> int:
    total = 0
    potencia = 1
    for coef in coefs:
        total += coef * potencia
        potencia *= x
    return total


if __name__ == "__main__":
    from _rodar import rodar

    rodar(polinomio=polinomio)
