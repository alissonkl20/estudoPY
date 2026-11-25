"""Solucao de logica/pleno/18_girar_horario.py. Tente resolver o enunciado antes de abrir."""

def girar_horario(matriz: list[list[int]]) -> list[list[int]]:
    if not matriz:
        return []
    n = len(matriz)
    if any(len(linha) != n for linha in matriz):
        raise ValueError("matriz invalida")
    return [[matriz[n - 1 - c][r] for c in range(n)] for r in range(n)]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(girar_horario=girar_horario)
