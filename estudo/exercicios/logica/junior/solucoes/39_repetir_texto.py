"""Solucao de logica/junior/39_repetir_texto.py. Tente resolver o enunciado antes de abrir."""

def repetir_texto(texto: str, n: int) -> str:
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n invalido")
    return texto * n


if __name__ == "__main__":
    from _rodar import rodar

    rodar(repetir_texto=repetir_texto)
