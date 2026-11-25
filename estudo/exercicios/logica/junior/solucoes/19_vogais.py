"""Solucao de logica/junior/19_vogais.py. Tente resolver o enunciado antes de abrir."""

def vogais(texto: str) -> int:
    return sum(ch.lower() in "aeiou" for ch in texto)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(vogais=vogais)
