"""Solucao de logica/junior/52_segundo_menor.py. Tente resolver o enunciado antes de abrir."""

def segundo_menor(nums: list[int]) -> int | None:
    unicos = sorted(set(nums))
    if len(unicos) < 2:
        return None
    return unicos[1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(segundo_menor=segundo_menor)
