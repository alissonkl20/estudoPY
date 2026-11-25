"""Solucao de logica/junior/64_comprimir.py. Tente resolver o enunciado antes de abrir."""

def comprimir(texto: str) -> list[list]:
    if not texto:
        return []
    saida = [[texto[0], 1]]
    for ch in texto[1:]:
        if ch == saida[-1][0]:
            saida[-1][1] += 1
        else:
            saida.append([ch, 1])
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(comprimir=comprimir)
