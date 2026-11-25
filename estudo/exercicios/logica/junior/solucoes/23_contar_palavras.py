"""Solucao de logica/junior/23_contar_palavras.py. Tente resolver o enunciado antes de abrir."""

def contar_palavras(texto: str) -> int:
    return len(texto.split())


if __name__ == "__main__":
    from _rodar import rodar

    rodar(contar_palavras=contar_palavras)
