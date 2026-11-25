"""Solucao de logica/junior/10_eh_primo.py. Tente resolver o enunciado antes de abrir."""

def eh_primo(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    from _rodar import rodar

    rodar(eh_primo=eh_primo)
