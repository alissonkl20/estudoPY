"""Solucao de logica/junior/60_decimal_para_binario.py. Tente resolver o enunciado antes de abrir."""

def decimal_para_binario(n: int) -> str:
    if n < 0:
        raise ValueError("n invalido")
    return bin(n)[2:]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(decimal_para_binario=decimal_para_binario)
