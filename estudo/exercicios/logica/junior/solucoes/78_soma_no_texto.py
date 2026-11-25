"""Solucao de logica/junior/78_soma_no_texto.py. Tente resolver o enunciado antes de abrir."""

def soma_no_texto(texto: str) -> int:
    total = 0
    atual = ""
    for ch in texto + " ":
        if ch.isdigit():
            atual += ch
        elif atual:
            total += int(atual)
            atual = ""
    return total


if __name__ == "__main__":
    from _rodar import rodar

    rodar(soma_no_texto=soma_no_texto)
