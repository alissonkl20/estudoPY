"""Solucao de logica/junior/17_limitar.py. Tente resolver o enunciado antes de abrir."""

def limitar(n: int, inicio: int, fim: int) -> int:
    if inicio > fim:
        raise ValueError("intervalo invalido")
    if n < inicio:
        return inicio
    if n > fim:
        return fim
    return n


if __name__ == "__main__":
    from _rodar import rodar

    rodar(limitar=limitar)
