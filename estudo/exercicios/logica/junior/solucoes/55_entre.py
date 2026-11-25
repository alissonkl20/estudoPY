"""Solucao de logica/junior/55_entre.py. Tente resolver o enunciado antes de abrir."""

def entre(n: int, inicio: int, fim: int) -> bool:
    return inicio <= n <= fim


if __name__ == "__main__":
    from _rodar import rodar

    rodar(entre=entre)
