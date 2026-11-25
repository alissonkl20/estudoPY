"""Solucao de logica/junior/28_mdc.py. Tente resolver o enunciado antes de abrir."""

def mdc(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        raise ValueError("mdc indefinido")
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    from _rodar import rodar

    rodar(mdc=mdc)
