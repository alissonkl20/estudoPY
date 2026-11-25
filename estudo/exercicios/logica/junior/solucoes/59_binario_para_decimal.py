"""Solucao de logica/junior/59_binario_para_decimal.py. Tente resolver o enunciado antes de abrir."""

def binario_para_decimal(texto: str) -> int:
    if not texto or any(ch not in "01" for ch in texto):
        raise ValueError("binario invalido")
    return int(texto, 2)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(binario_para_decimal=binario_para_decimal)
