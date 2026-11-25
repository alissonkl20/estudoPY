"""Solucao de logica/junior/12_soma_digitos.py. Tente resolver o enunciado antes de abrir."""

def soma_digitos(n: int) -> int:
    return sum(int(ch) for ch in str(abs(n)))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(soma_digitos=soma_digitos)
