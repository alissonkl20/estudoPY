"""Solucao de logica/junior/13_contar_digitos.py. Tente resolver o enunciado antes de abrir."""

def contar_digitos(n: int) -> int:
    return len(str(abs(n)))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(contar_digitos=contar_digitos)
