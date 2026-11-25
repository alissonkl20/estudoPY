"""Solucao de logica/junior/33_tipo_triangulo.py. Tente resolver o enunciado antes de abrir."""

def tipo_triangulo(a: int, b: int, c: int) -> str:
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("triangulo invalido")
    lados = len({a, b, c})
    if lados == 1:
        return "equilatero"
    if lados == 2:
        return "isosceles"
    return "escaleno"


if __name__ == "__main__":
    from _rodar import rodar

    rodar(tipo_triangulo=tipo_triangulo)
