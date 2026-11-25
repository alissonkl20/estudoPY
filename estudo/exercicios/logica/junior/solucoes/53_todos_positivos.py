"""Solucao de logica/junior/53_todos_positivos.py. Tente resolver o enunciado antes de abrir."""

def todos_positivos(nums: list[int]) -> bool:
    return all(n > 0 for n in nums)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(todos_positivos=todos_positivos)
