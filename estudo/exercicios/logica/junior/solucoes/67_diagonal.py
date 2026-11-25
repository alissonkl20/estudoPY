"""Solucao de logica/junior/67_diagonal.py. Tente resolver o enunciado antes de abrir."""

def diagonal(matriz: list[list[int]]) -> int:
    if not matriz or any(len(linha) != len(matriz) for linha in matriz):
        raise ValueError("matriz invalida")
    return sum(matriz[i][i] for i in range(len(matriz)))


if __name__ == "__main__":
    from _rodar import rodar

    rodar(diagonal=diagonal)
