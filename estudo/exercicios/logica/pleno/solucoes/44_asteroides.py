"""Solucao de logica/pleno/44_asteroides.py. Tente resolver o enunciado antes de abrir."""

def asteroides(nums: list[int]) -> list[int]:
    pilha = []
    for n in nums:
        vivo = True
        while vivo and pilha and pilha[-1] > 0 and n < 0:
            if pilha[-1] < -n:
                pilha.pop()
                continue
            if pilha[-1] == -n:
                pilha.pop()
            vivo = False
        if vivo:
            pilha.append(n)
    return pilha


if __name__ == "__main__":
    from _rodar import rodar

    rodar(asteroides=asteroides)
