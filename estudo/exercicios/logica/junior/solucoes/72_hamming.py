"""Solucao de logica/junior/72_hamming.py. Tente resolver o enunciado antes de abrir."""

def hamming(a: str, b: str) -> int:
    if len(a) != len(b):
        raise ValueError("tamanhos diferentes")
    return sum(x != y for x, y in zip(a, b))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(hamming=hamming)
