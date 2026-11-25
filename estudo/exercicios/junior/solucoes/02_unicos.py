"""Solucao de junior/02_unicos.py. Tente resolver o enunciado antes de abrir."""


def unicos(itens: list) -> list:
    vistos = []
    for item in itens:
        if item not in vistos:
            vistos.append(item)
    return vistos


if __name__ == "__main__":
    from _rodar import rodar

    rodar(unicos=unicos)
