"""Solucao de logica/pleno/80_sequencia_pilha.py. Tente resolver o enunciado antes de abrir."""

def sequencia_pilha(pushed: list[int], popped: list[int]) -> bool:
    if len(pushed) != len(popped):
        raise ValueError("tamanhos diferentes")
    pilha = []
    i = 0
    for n in pushed:
        pilha.append(n)
        while pilha and i < len(popped) and pilha[-1] == popped[i]:
            pilha.pop()
            i += 1
    return i == len(popped)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(sequencia_pilha=sequencia_pilha)
