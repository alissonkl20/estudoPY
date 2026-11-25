"""Solucao de logica/pleno/20_kesimo_maior.py. Tente resolver o enunciado antes de abrir."""

def kesimo_maior(nums: list[int], k: int) -> int:
    distintos = sorted(set(nums), reverse=True)
    if k < 1 or k > len(distintos):
        raise ValueError("k invalido")
    return distintos[k - 1]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(kesimo_maior=kesimo_maior)
