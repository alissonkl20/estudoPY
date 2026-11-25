"""Solucao de logica/junior/38_remover_vogais.py. Tente resolver o enunciado antes de abrir."""

def remover_vogais(texto: str) -> str:
    return "".join(ch for ch in texto if ch.lower() not in "aeiou")


if __name__ == "__main__":
    from _rodar import rodar

    rodar(remover_vogais=remover_vogais)
