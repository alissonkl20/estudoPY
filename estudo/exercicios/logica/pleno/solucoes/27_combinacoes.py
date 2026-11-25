"""Solucao de logica/pleno/27_combinacoes.py. Tente resolver o enunciado antes de abrir."""

def combinacoes(n: int, k: int) -> list[list[int]]:
    if n < 0 or k < 0 or k > n:
        raise ValueError("intervalo invalido")
    saida = []

    def montar(inicio: int, atual: list[int]) -> None:
        if len(atual) == k:
            saida.append(atual)
            return
        for numero in range(inicio, n + 1):
            montar(numero + 1, atual + [numero])

    montar(1, [])
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(combinacoes=combinacoes)
