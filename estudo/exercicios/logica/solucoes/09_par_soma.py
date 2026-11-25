"""Solucao de logica/09_par_soma.py. Tente resolver o enunciado antes de abrir."""


def indices_que_somam(nums: list[int], alvo: int) -> tuple[int, int] | None:
    vistos: dict[int, int] = {}
    for j, num in enumerate(nums):
        complemento = alvo - num
        if complemento in vistos:
            return (vistos[complemento], j)
        if num not in vistos:
            vistos[num] = j
    return None


if __name__ == "__main__":
    from _rodar import rodar

    rodar(indices_que_somam=indices_que_somam)
