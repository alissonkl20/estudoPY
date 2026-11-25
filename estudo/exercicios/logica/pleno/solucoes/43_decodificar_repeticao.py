"""Solucao de logica/pleno/43_decodificar_repeticao.py. Tente resolver o enunciado antes de abrir."""

def decodificar_repeticao(texto: str) -> str:
    pilha = []
    atual = ""
    k = 0
    for ch in texto:
        if ch.isdigit():
            k = k * 10 + int(ch)
        elif ch == "[":
            pilha.append((atual, k))
            atual = ""
            k = 0
        elif ch == "]":
            if not pilha:
                raise ValueError("expressao invalida")
            anterior, vezes = pilha.pop()
            if vezes < 1:
                raise ValueError("expressao invalida")
            atual = anterior + atual * vezes
        else:
            atual += ch
    if pilha or k:
        raise ValueError("expressao invalida")
    return atual


if __name__ == "__main__":
    from _rodar import rodar

    rodar(decodificar_repeticao=decodificar_repeticao)
