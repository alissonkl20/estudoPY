"""Solucao de logica/pleno/60_fatores_primos.py. Tente resolver o enunciado antes de abrir."""

def fatores_primos(n: int) -> list[int]:
    if n < 1:
        raise ValueError("n invalido")
    saida = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            saida.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        saida.append(n)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(fatores_primos=fatores_primos)
