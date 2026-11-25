"""Solucao de logica/junior/06_inverter_texto.py. Tente resolver o enunciado antes de abrir."""

def inverter_texto(texto: str) -> str:
    return texto[::-1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(inverter_texto=inverter_texto)
