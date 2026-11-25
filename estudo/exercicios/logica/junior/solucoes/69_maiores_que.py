"""Solucao de logica/junior/69_maiores_que.py. Tente resolver o enunciado antes de abrir."""

def maiores_que(nums: list[int], limite: int) -> list[int]:
    return [n for n in nums if n > limite]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(maiores_que=maiores_que)
