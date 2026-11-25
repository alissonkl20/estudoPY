"""Solucao de logica/01_sequencia.py. Tente resolver o enunciado antes de abrir."""


def classificar(n: int) -> str:
    partes = []
    if n % 3 == 0:
        partes.append("Fizz")
    if n % 5 == 0:
        partes.append("Buzz")
    if n % 7 == 0:
        partes.append("Pop")
    return "".join(partes) if partes else str(n)


def sequencia(ate: int) -> list[str]:
    if ate < 1:
        raise ValueError("ate deve ser >= 1")
    return [classificar(n) for n in range(1, ate + 1)]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(classificar=classificar, sequencia=sequencia)
