"""Solucao de logica/pleno/70_palindromo_flexivel.py. Tente resolver o enunciado antes de abrir."""

def palindromo_flexivel(texto: str) -> bool:
    def faixa(esq: int, dir_: int) -> bool:
        while esq < dir_:
            if texto[esq] != texto[dir_]:
                return False
            esq += 1
            dir_ -= 1
        return True

    i, j = 0, len(texto) - 1
    while i < j:
        if texto[i] != texto[j]:
            return faixa(i + 1, j) or faixa(i, j - 1)
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    from _rodar import rodar

    rodar(palindromo_flexivel=palindromo_flexivel)
