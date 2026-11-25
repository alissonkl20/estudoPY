"""Solucao de logica/junior/79_produto_lista.py. Tente resolver o enunciado antes de abrir."""

def produto_lista(nums: list[int]) -> int:
    total = 1
    for n in nums:
        total *= n
    return total


if __name__ == "__main__":
    from _rodar import rodar

    rodar(produto_lista=produto_lista)
