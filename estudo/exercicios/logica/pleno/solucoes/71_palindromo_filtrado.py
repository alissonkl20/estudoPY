"""Solucao de logica/pleno/71_palindromo_filtrado.py. Tente resolver o enunciado antes de abrir."""

def palindromo_filtrado(texto: str) -> bool:
    limpo = "".join(ch.lower() for ch in texto if ch.isalnum())
    return limpo == limpo[::-1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(palindromo_filtrado=palindromo_filtrado)
