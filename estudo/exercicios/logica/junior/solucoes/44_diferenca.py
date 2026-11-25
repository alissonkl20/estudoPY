"""Solucao de logica/junior/44_diferenca.py. Tente resolver o enunciado antes de abrir."""

def diferenca(a: list, b: list) -> list:
    bloqueados = set(b)
    vistos = set()
    saida = []
    for item in a:
        if item not in bloqueados and item not in vistos:
            vistos.add(item)
            saida.append(item)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(diferenca=diferenca)
