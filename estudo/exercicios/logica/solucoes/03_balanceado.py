"""Solucao de logica/03_balanceado.py. Tente resolver o enunciado antes de abrir."""


def balanceado(texto: str) -> bool:
    pares = {")": "(", "]": "[", "}": "{"}
    pilha: list[str] = []
    for caractere in texto:
        if caractere in "([{":
            pilha.append(caractere)
        elif caractere in pares:
            if not pilha or pilha[-1] != pares[caractere]:
                return False
            pilha.pop()
    return not pilha


if __name__ == "__main__":
    from _rodar import rodar

    rodar(balanceado=balanceado)
