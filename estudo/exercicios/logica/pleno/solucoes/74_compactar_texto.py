"""Solucao de logica/pleno/74_compactar_texto.py. Tente resolver o enunciado antes de abrir."""

def compactar_texto(texto: str) -> str:
    if not texto:
        return ""
    blocos = []
    atual = texto[0]
    qtd = 1
    for ch in texto[1:]:
        if ch == atual:
            qtd += 1
        else:
            blocos.append(atual + str(qtd))
            atual = ch
            qtd = 1
    blocos.append(atual + str(qtd))
    compacto = "".join(blocos)
    return compacto if len(compacto) < len(texto) else texto


if __name__ == "__main__":
    from _rodar import rodar

    rodar(compactar_texto=compactar_texto)
