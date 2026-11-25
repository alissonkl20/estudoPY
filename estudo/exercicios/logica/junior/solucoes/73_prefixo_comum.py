"""Solucao de logica/junior/73_prefixo_comum.py. Tente resolver o enunciado antes de abrir."""

def prefixo_comum(a: str, b: str) -> str:
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return a[:i]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(prefixo_comum=prefixo_comum)
