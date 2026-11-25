"""Solucao de logica/pleno/08_eh_subsequencia.py. Tente resolver o enunciado antes de abrir."""

def eh_subsequencia(padrao: str, texto: str) -> bool:
    i = 0
    for ch in texto:
        if i < len(padrao) and ch == padrao[i]:
            i += 1
    return i == len(padrao)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(eh_subsequencia=eh_subsequencia)
