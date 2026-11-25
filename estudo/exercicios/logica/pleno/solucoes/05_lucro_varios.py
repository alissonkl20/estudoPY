"""Solucao de logica/pleno/05_lucro_varios.py. Tente resolver o enunciado antes de abrir."""

def lucro_varios(precos: list[int]) -> int:
    total = 0
    for i in range(1, len(precos)):
        if precos[i] > precos[i - 1]:
            total += precos[i] - precos[i - 1]
    return total


if __name__ == "__main__":
    from _rodar import rodar

    rodar(lucro_varios=lucro_varios)
