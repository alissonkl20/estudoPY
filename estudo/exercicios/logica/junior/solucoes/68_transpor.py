"""Solucao de logica/junior/68_transpor.py. Tente resolver o enunciado antes de abrir."""

def transpor(matriz: list[list[int]]) -> list[list[int]]:
    if not matriz:
        return []
    largura = len(matriz[0])
    if any(len(linha) != largura for linha in matriz):
        raise ValueError("matriz irregular")
    return [[matriz[r][c] for r in range(len(matriz))] for c in range(largura)]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(transpor=transpor)
