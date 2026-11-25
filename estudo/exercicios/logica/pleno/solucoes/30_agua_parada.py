"""Solucao de logica/pleno/30_agua_parada.py. Tente resolver o enunciado antes de abrir."""

def agua_parada(alturas: list[int]) -> int:
    if not alturas:
        return 0
    esquerda, direita = 0, len(alturas) - 1
    max_esq = max_dir = agua = 0
    while esquerda < direita:
        if alturas[esquerda] <= alturas[direita]:
            max_esq = max(max_esq, alturas[esquerda])
            agua += max_esq - alturas[esquerda]
            esquerda += 1
        else:
            max_dir = max(max_dir, alturas[direita])
            agua += max_dir - alturas[direita]
            direita -= 1
    return agua


if __name__ == "__main__":
    from _rodar import rodar

    rodar(agua_parada=agua_parada)
