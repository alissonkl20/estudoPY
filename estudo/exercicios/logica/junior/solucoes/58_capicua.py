"""Solucao de logica/junior/58_capicua.py. Tente resolver o enunciado antes de abrir."""

def capicua(n: int) -> bool:
    if n < 0:
        return False
    texto = str(n)
    return texto == texto[::-1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(capicua=capicua)
