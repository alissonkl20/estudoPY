"""Solucao de logica/junior/37_contar_letra.py. Tente resolver o enunciado antes de abrir."""

def contar_letra(texto: str, letra: str) -> int:
    if len(letra) != 1:
        raise ValueError("letra invalida")
    alvo = letra.lower()
    return sum(ch.lower() == alvo for ch in texto)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(contar_letra=contar_letra)
