"""Solucao de logica/05_frequencia.py. Tente resolver o enunciado antes de abrir."""


def segundo_maior(nums: list[int]) -> int | None:
    maior = None
    segundo = None
    for num in nums:
        if maior is None or num > maior:
            segundo = maior
            maior = num
        elif num != maior and (segundo is None or num > segundo):
            segundo = num
    return segundo


def mais_frequente(itens: list):
    if not itens:
        raise ValueError("lista vazia")
    contagem: dict = {}
    for item in itens:
        contagem[item] = contagem.get(item, 0) + 1
    melhor = itens[0]
    for item in itens:
        if contagem[item] > contagem[melhor]:
            melhor = item
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(segundo_maior=segundo_maior, mais_frequente=mais_frequente)
