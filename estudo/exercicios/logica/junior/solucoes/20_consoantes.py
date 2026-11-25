"""Solucao de logica/junior/20_consoantes.py. Tente resolver o enunciado antes de abrir."""

def consoantes(texto: str) -> int:
    return sum(ch.isalpha() and ch.lower() not in "aeiou" for ch in texto)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(consoantes=consoantes)
