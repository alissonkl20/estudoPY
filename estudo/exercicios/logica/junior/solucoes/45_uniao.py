"""Solucao de logica/junior/45_uniao.py. Tente resolver o enunciado antes de abrir."""

def uniao(a: list, b: list) -> list:
    vistos = set()
    saida = []
    for item in list(a) + list(b):
        if item not in vistos:
            vistos.add(item)
            saida.append(item)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(uniao=uniao)
