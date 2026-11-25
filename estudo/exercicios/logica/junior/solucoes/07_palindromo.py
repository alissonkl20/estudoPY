"""Solucao de logica/junior/07_palindromo.py. Tente resolver o enunciado antes de abrir."""

def palindromo(texto: str) -> bool:
    limpo = "".join(ch.lower() for ch in texto if ch.isalnum())
    return limpo == limpo[::-1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(palindromo=palindromo)
