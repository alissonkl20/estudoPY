"""Solucao de logica/pleno/45_dias_quentes.py. Tente resolver o enunciado antes de abrir."""

def dias_quentes(temps: list[int]) -> list[int]:
    saida = [0] * len(temps)
    pilha = []
    for i, temp in enumerate(temps):
        while pilha and temps[pilha[-1]] < temp:
            j = pilha.pop()
            saida[j] = i - j
        pilha.append(i)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(dias_quentes=dias_quentes)
