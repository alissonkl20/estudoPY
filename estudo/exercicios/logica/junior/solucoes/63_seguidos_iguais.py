"""Solucao de logica/junior/63_seguidos_iguais.py. Tente resolver o enunciado antes de abrir."""

def seguidos_iguais(itens: list) -> bool:
    return any(itens[i] == itens[i + 1] for i in range(len(itens) - 1))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(seguidos_iguais=seguidos_iguais)
