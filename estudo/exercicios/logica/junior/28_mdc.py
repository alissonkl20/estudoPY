"""
Logica junior 28 — Maximo divisor comum

Use o valor absoluto. mdc(0, 0) levanta ValueError. mdc(0, 5) vale 5.

Como testar:
    python3 logica/junior/28_mdc.py
"""

def mdc(a: int, b: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = mdc(12, 8)
    _verificar(veio == 4, f"mdc(12, 8) -> 4, veio {veio!r}", falhas)
    veio = mdc(17, 19)
    _verificar(veio == 1, f"mdc(17, 19) -> 1, veio {veio!r}", falhas)
    veio = mdc(0, 5)
    _verificar(veio == 5, f"mdc(0, 5) -> 5, veio {veio!r}", falhas)
    veio = mdc(-4, 6)
    _verificar(veio == 2, f"mdc(-4, 6) -> 2, veio {veio!r}", falhas)
    try:
        mdc(0, 0)
        _verificar(False, "mdc(0, 0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "mdc(0, 0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

