"""Solucao de logica/junior/31_soma_quadrados.py. Tente resolver o enunciado antes de abrir."""

def soma_quadrados(n: int) -> int:
    if n < 0:
        raise ValueError("n invalido")
    return sum(i * i for i in range(1, n + 1))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(soma_quadrados=soma_quadrados)
