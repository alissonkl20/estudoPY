"""
Logica pleno 59 — Potencia modular

Devolva base elevado a exp, modulo mod. exp igual a 0 vale 1. exp negativo ou mod menor que 1 levanta ValueError.

Como testar:
    python3 logica/pleno/59_potencia_modular.py
"""

def potencia_modular(base: int, exp: int, mod: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = potencia_modular(2, 10, 1000)
    _verificar(veio == 24, f"potencia_modular(2, 10, 1000) -> 24, veio {veio!r}", falhas)
    veio = potencia_modular(2, 0, 5)
    _verificar(veio == 1, f"potencia_modular(2, 0, 5) -> 1, veio {veio!r}", falhas)
    veio = potencia_modular(5, 3, 13)
    _verificar(veio == 8, f"potencia_modular(5, 3, 13) -> 8, veio {veio!r}", falhas)
    try:
        potencia_modular(2, -1, 5)
        _verificar(False, "potencia_modular(2, -1, 5) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "potencia_modular(2, -1, 5) levanta ValueError", falhas)
    try:
        potencia_modular(2, 3, 0)
        _verificar(False, "potencia_modular(2, 3, 0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "potencia_modular(2, 3, 0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

