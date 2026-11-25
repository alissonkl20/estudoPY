"""Solucao de logica/pleno/29_comprimento_palindromo.py. Tente resolver o enunciado antes de abrir."""

def comprimento_palindromo(texto: str) -> int:
    if not texto:
        return 0
    melhor = 1
    n = len(texto)
    for centro in range(n):
        for esq, dir_ in ((centro, centro), (centro, centro + 1)):
            while esq >= 0 and dir_ < n and texto[esq] == texto[dir_]:
                melhor = max(melhor, dir_ - esq + 1)
                esq -= 1
                dir_ += 1
    return melhor


if __name__ == "__main__":
    from _rodar import rodar

    rodar(comprimento_palindromo=comprimento_palindromo)
