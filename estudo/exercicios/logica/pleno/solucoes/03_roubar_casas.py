"""Solucao de logica/pleno/03_roubar_casas.py. Tente resolver o enunciado antes de abrir."""

def roubar_casas(casas: list[int]) -> int:
    anterior = atual = 0
    for valor in casas:
        anterior, atual = atual, max(atual, anterior + valor)
    return atual


if __name__ == "__main__":
    from _rodar import rodar

    rodar(roubar_casas=roubar_casas)
