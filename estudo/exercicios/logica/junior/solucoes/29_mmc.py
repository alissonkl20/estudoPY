"""Solucao de logica/junior/29_mmc.py. Tente resolver o enunciado antes de abrir."""

def mmc(a: int, b: int) -> int:
    if a == 0 and b == 0:
        raise ValueError("mmc indefinido")
    aa, bb = abs(a), abs(b)
    x, y = aa, bb
    while y:
        x, y = y, x % y
    if x == 0:
        return 0
    return aa // x * bb


if __name__ == "__main__":
    from _rodar import rodar

    rodar(mmc=mmc)
