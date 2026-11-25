"""Solucao de logica/pleno/69_uma_edicao.py. Tente resolver o enunciado antes de abrir."""

def uma_edicao(a: str, b: str) -> bool:
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) <= 1
    if len(a) > len(b):
        a, b = b, a
    i = j = 0
    usado = False
    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if usado:
                return False
            usado = True
            j += 1
        else:
            i += 1
            j += 1
    return True


if __name__ == "__main__":
    from _rodar import rodar

    rodar(uma_edicao=uma_edicao)
