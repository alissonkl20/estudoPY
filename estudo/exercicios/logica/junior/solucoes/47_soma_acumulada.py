"""Solucao de logica/junior/47_soma_acumulada.py. Tente resolver o enunciado antes de abrir."""

def soma_acumulada(nums: list[int]) -> list[int]:
    total = 0
    saida = []
    for n in nums:
        total += n
        saida.append(total)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(soma_acumulada=soma_acumulada)
