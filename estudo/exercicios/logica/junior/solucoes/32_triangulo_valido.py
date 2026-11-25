"""Solucao de logica/junior/32_triangulo_valido.py. Tente resolver o enunciado antes de abrir."""

def triangulo_valido(a: int, b: int, c: int) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


if __name__ == "__main__":
    from _rodar import rodar

    rodar(triangulo_valido=triangulo_valido)
