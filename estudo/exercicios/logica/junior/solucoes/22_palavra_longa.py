"""Solucao de logica/junior/22_palavra_longa.py. Tente resolver o enunciado antes de abrir."""

def palavra_longa(texto: str) -> str:
    palavras = texto.split()
    if not palavras:
        raise ValueError("sem palavra")
    melhor = palavras[0]
    for palavra in palavras[1:]:
        if len(palavra) > len(melhor):
            melhor = palavra
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(palavra_longa=palavra_longa)
