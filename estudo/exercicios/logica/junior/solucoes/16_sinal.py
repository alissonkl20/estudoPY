"""Solucao de logica/junior/16_sinal.py. Tente resolver o enunciado antes de abrir."""

def sinal(n: int) -> str:
    if n > 0:
        return "positivo"
    if n < 0:
        return "negativo"
    return "zero"


if __name__ == "__main__":
    from _rodar import rodar

    rodar(sinal=sinal)
