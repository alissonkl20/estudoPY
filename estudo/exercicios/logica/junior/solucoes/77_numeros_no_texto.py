"""Solucao de logica/junior/77_numeros_no_texto.py. Tente resolver o enunciado antes de abrir."""

def numeros_no_texto(texto: str) -> list[int]:
    saida = []
    atual = ""
    for ch in texto:
        if ch.isdigit():
            atual += ch
        elif atual:
            saida.append(int(atual))
            atual = ""
    if atual:
        saida.append(int(atual))
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(numeros_no_texto=numeros_no_texto)
