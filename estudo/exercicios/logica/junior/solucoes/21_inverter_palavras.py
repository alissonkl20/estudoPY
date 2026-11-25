"""Solucao de logica/junior/21_inverter_palavras.py. Tente resolver o enunciado antes de abrir."""

def inverter_palavras(texto: str) -> str:
    return " ".join(reversed(texto.split()))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(inverter_palavras=inverter_palavras)
