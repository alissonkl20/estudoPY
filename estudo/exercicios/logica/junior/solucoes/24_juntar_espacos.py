"""Solucao de logica/junior/24_juntar_espacos.py. Tente resolver o enunciado antes de abrir."""

def juntar_espacos(texto: str) -> str:
    return " ".join(texto.split())


if __name__ == "__main__":
    from _rodar import rodar

    rodar(juntar_espacos=juntar_espacos)
