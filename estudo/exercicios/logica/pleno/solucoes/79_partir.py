"""Solucao de logica/pleno/79_partir.py. Tente resolver o enunciado antes de abrir."""

def partir(nums: list[int], pivo: int) -> tuple[list[int], list[int], list[int]]:
    menores, iguais, maiores = [], [], []
    for n in nums:
        if n < pivo:
            menores.append(n)
        elif n == pivo:
            iguais.append(n)
        else:
            maiores.append(n)
    return (menores, iguais, maiores)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(partir=partir)
