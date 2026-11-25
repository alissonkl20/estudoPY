"""Solucao de logica/pleno/75_zigzag.py. Tente resolver o enunciado antes de abrir."""

def zigzag(texto: str, linhas: int) -> str:
    if linhas < 1:
        raise ValueError("linhas invalidas")
    if linhas == 1 or linhas >= len(texto):
        return texto
    faixas = [""] * linhas
    i = 0
    passo = 1
    for ch in texto:
        faixas[i] += ch
        if i == 0:
            passo = 1
        elif i == linhas - 1:
            passo = -1
        i += passo
    return "".join(faixas)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(zigzag=zigzag)
