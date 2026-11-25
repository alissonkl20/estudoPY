"""Solucao de logica/pleno/32_trios_soma.py. Tente resolver o enunciado antes de abrir."""

def trios_soma(nums: list[int]) -> list[list[int]]:
    ordenados = sorted(nums)
    saida = []
    for i in range(len(ordenados)):
        if i and ordenados[i] == ordenados[i - 1]:
            continue
        esquerda, direita = i + 1, len(ordenados) - 1
        while esquerda < direita:
            soma = ordenados[i] + ordenados[esquerda] + ordenados[direita]
            if soma == 0:
                saida.append([ordenados[i], ordenados[esquerda], ordenados[direita]])
                esquerda += 1
                direita -= 1
                while esquerda < direita and ordenados[esquerda] == ordenados[esquerda - 1]:
                    esquerda += 1
                while esquerda < direita and ordenados[direita] == ordenados[direita + 1]:
                    direita -= 1
            elif soma < 0:
                esquerda += 1
            else:
                direita -= 1
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(trios_soma=trios_soma)
