"""Solucao de logica/junior/05_contar_ocorrencias.py. Tente resolver o enunciado antes de abrir."""

def contar_ocorrencias(itens: list, alvo) -> int:
    return sum(1 for item in itens if item == alvo)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(contar_ocorrencias=contar_ocorrencias)
