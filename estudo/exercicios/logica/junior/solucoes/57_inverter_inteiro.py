"""Solucao de logica/junior/57_inverter_inteiro.py. Tente resolver o enunciado antes de abrir."""

def inverter_inteiro(n: int) -> int:
    sinal = -1 if n < 0 else 1
    return sinal * int(str(abs(n))[::-1])


if __name__ == "__main__":
    from _rodar import rodar

    rodar(inverter_inteiro=inverter_inteiro)
