"""Solucao de logica/pleno/49_retangulo_histograma.py. Tente resolver o enunciado antes de abrir."""

def retangulo_histograma(alturas: list[int]) -> int:
    pilha = [-1]
    melhor = 0
    for i, altura in enumerate(alturas + [0]):
        while pilha[-1] != -1 and alturas[pilha[-1]] > altura:
            h = alturas[pilha.pop()]
            melhor = max(melhor, h * (i - pilha[-1] - 1))
        pilha.append(i)
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(retangulo_histograma=retangulo_histograma)
