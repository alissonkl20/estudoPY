"""Solucao de logica/junior/61_bits_um.py. Tente resolver o enunciado antes de abrir."""

def bits_um(n: int) -> int:
    if n < 0:
        raise ValueError("n invalido")
    return bin(n).count("1")


if __name__ == "__main__":
    from _rodar import rodar

    rodar(bits_um=bits_um)
