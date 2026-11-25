"""Solucao de logica/pleno/59_potencia_modular.py. Tente resolver o enunciado antes de abrir."""

def potencia_modular(base: int, exp: int, mod: int) -> int:
    if exp < 0 or mod < 1:
        raise ValueError("entrada invalida")
    return pow(base, exp, mod)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(potencia_modular=potencia_modular)
