"""Solucao de logica/pleno/64_raizes_inteiras.py. Tente resolver o enunciado antes de abrir."""

def raizes_inteiras(a: int, b: int, c: int) -> list[int]:
    if a == 0:
        raise ValueError("a invalido")
    discriminante = b * b - 4 * a * c
    if discriminante < 0:
        return []
    raiz = int(discriminante ** 0.5)
    if raiz * raiz != discriminante:
        return []
    saida = []
    for numerador in (-b - raiz, -b + raiz):
        if numerador % (2 * a) == 0:
            valor = numerador // (2 * a)
            if valor not in saida:
                saida.append(valor)
    return sorted(saida)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(raizes_inteiras=raizes_inteiras)
