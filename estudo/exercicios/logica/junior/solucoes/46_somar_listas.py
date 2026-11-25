"""Solucao de logica/junior/46_somar_listas.py. Tente resolver o enunciado antes de abrir."""

def somar_listas(a: list[int], b: list[int]) -> list[int]:
    if len(a) != len(b):
        raise ValueError("tamanhos diferentes")
    return [x + y for x, y in zip(a, b)]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(somar_listas=somar_listas)
