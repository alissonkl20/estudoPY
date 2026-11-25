"""Solucao de logica/pleno/38_maximos_janela.py. Tente resolver o enunciado antes de abrir."""

def maximos_janela(nums: list[int], k: int) -> list[int]:
    if k < 1 or k > len(nums):
        raise ValueError("janela invalida")
    from collections import deque
    fila = deque()
    saida = []
    for i, n in enumerate(nums):
        while fila and fila[0] <= i - k:
            fila.popleft()
        while fila and nums[fila[-1]] <= n:
            fila.pop()
        fila.append(i)
        if i >= k - 1:
            saida.append(nums[fila[0]])
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(maximos_janela=maximos_janela)
