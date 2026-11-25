"""Solucao de logica/pleno/31_maior_area.py. Tente resolver o enunciado antes de abrir."""

def maior_area(alturas: list[int]) -> int:
    esquerda, direita = 0, len(alturas) - 1
    melhor = 0
    while esquerda < direita:
        altura = alturas[esquerda] if alturas[esquerda] < alturas[direita] else alturas[direita]
        melhor = max(melhor, altura * (direita - esquerda))
        if alturas[esquerda] <= alturas[direita]:
            esquerda += 1
        else:
            direita -= 1
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(maior_area=maior_area)
