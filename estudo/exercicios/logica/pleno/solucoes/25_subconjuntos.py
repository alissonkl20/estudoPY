"""Solucao de logica/pleno/25_subconjuntos.py. Tente resolver o enunciado antes de abrir."""

def subconjuntos(nums: list[int]) -> list[list[int]]:
    saida = [[]]
    for n in sorted(nums):
        saida += [grupo + [n] for grupo in saida]
    saida.sort(key=lambda grupo: (len(grupo), grupo))
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(subconjuntos=subconjuntos)
