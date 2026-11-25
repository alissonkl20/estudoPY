"""
Logica junior 29 — Minimo multiplo comum

mmc(0, 0) levanta ValueError. mmc(0, 5) vale 0. O resultado e nao negativo.

Como testar:
    python3 logica/junior/29_mmc.py
"""

def mmc(a: int, b: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = mmc(4, 6)
    _verificar(veio == 12, f"mmc(4, 6) -> 12, veio {veio!r}", falhas)
    veio = mmc(0, 5)
    _verificar(veio == 0, f"mmc(0, 5) -> 0, veio {veio!r}", falhas)
    veio = mmc(7, 3)
    _verificar(veio == 21, f"mmc(7, 3) -> 21, veio {veio!r}", falhas)
    veio = mmc(-2, 4)
    _verificar(veio == 4, f"mmc(-2, 4) -> 4, veio {veio!r}", falhas)
    try:
        mmc(0, 0)
        _verificar(False, "mmc(0, 0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "mmc(0, 0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

