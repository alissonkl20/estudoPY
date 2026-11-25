"""
Logica pleno 64 — Raizes inteiras

Resolva a*x*x + b*x + c = 0. Devolva as raizes inteiras, sem repetir, em ordem. Se a for 0, levante ValueError. Se nao houver raiz inteira, [].

Como testar:
    python3 logica/pleno/64_raizes_inteiras.py
"""

def raizes_inteiras(a: int, b: int, c: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = raizes_inteiras(1, -3, 2)
    _verificar(veio == [1, 2], f"raizes_inteiras(1, -3, 2) -> [1, 2], veio {veio!r}", falhas)
    veio = raizes_inteiras(1, -2, 1)
    _verificar(veio == [1], f"raizes_inteiras(1, -2, 1) -> [1], veio {veio!r}", falhas)
    veio = raizes_inteiras(1, 2, 1)
    _verificar(veio == [-1], f"raizes_inteiras(1, 2, 1) -> [-1], veio {veio!r}", falhas)
    veio = raizes_inteiras(1, 0, 1)
    _verificar(veio == [], f"raizes_inteiras(1, 0, 1) -> [], veio {veio!r}", falhas)
    try:
        raizes_inteiras(0, 1, 1)
        _verificar(False, "raizes_inteiras(0, 1, 1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "raizes_inteiras(0, 1, 1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

