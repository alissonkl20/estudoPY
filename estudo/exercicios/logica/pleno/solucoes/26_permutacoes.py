"""Solucao de logica/pleno/26_permutacoes.py. Tente resolver o enunciado antes de abrir."""

def permutacoes(nums: list[int]) -> list[list[int]]:
    saida = []

    def montar(restante: list[int], atual: list[int]) -> None:
        if not restante:
            saida.append(atual)
            return
        for i, n in enumerate(restante):
            montar(restante[:i] + restante[i + 1 :], atual + [n])

    montar(sorted(nums), [])
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(permutacoes=permutacoes)
