"""Solucao de logica/junior/25_so_digitos.py. Tente resolver o enunciado antes de abrir."""

def so_digitos(texto: str) -> bool:
    return texto.isdigit()


if __name__ == "__main__":
    from _rodar import rodar

    rodar(so_digitos=so_digitos)
