"""Solucao de logica/junior/43_intersecao.py. Tente resolver o enunciado antes de abrir."""

def intersecao(a: list, b: list) -> list:
    presentes = set(b)
    vistos = set()
    saida = []
    for item in a:
        if item in presentes and item not in vistos:
            vistos.add(item)
            saida.append(item)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(intersecao=intersecao)
