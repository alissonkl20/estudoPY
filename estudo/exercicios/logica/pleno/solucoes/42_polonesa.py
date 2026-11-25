"""Solucao de logica/pleno/42_polonesa.py. Tente resolver o enunciado antes de abrir."""

def polonesa(tokens: list[str]) -> int:
    pilha = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            if len(pilha) < 2:
                raise ValueError("expressao invalida")
            b = pilha.pop()
            a = pilha.pop()
            if token == "+":
                pilha.append(a + b)
            elif token == "-":
                pilha.append(a - b)
            elif token == "*":
                pilha.append(a * b)
            else:
                if b == 0:
                    raise ValueError("divisao por zero")
                pilha.append(int(a / b))
        else:
            try:
                pilha.append(int(token))
            except ValueError as erro:
                raise ValueError("expressao invalida") from erro
    if len(pilha) != 1:
        raise ValueError("expressao invalida")
    return pilha[0]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(polonesa=polonesa)
