"""Solucao de logica/pleno/04_lucro_unico.py. Tente resolver o enunciado antes de abrir."""

def lucro_unico(precos: list[int]) -> int:
    if not precos:
        return 0
    menor = precos[0]
    melhor = 0
    for preco in precos[1:]:
        if preco - menor > melhor:
            melhor = preco - menor
        if preco < menor:
            menor = preco
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(lucro_unico=lucro_unico)
