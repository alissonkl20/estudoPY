"""Solucao de logica/pleno/35_consegue_chegar.py. Tente resolver o enunciado antes de abrir."""

def consegue_chegar(nums: list[int]) -> bool:
    alcance = 0
    for i, passo in enumerate(nums):
        if i > alcance:
            return False
        alcance = max(alcance, i + passo)
    return True


if __name__ == "__main__":
    from _rodar import rodar

    rodar(consegue_chegar=consegue_chegar)
