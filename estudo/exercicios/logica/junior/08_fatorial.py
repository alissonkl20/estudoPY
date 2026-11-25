"""
Logica junior 08 — Fatorial

fatorial(0) vale 1. n menor que 0 levanta ValueError.

Como testar:
    python3 logica/junior/08_fatorial.py
"""

def fatorial(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = fatorial(0)
    _verificar(veio == 1, f"fatorial(0) -> 1, veio {veio!r}", falhas)
    veio = fatorial(1)
    _verificar(veio == 1, f"fatorial(1) -> 1, veio {veio!r}", falhas)
    veio = fatorial(5)
    _verificar(veio == 120, f"fatorial(5) -> 120, veio {veio!r}", falhas)
    veio = fatorial(7)
    _verificar(veio == 5040, f"fatorial(7) -> 5040, veio {veio!r}", falhas)
    try:
        fatorial(-1)
        _verificar(False, "fatorial(-1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "fatorial(-1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

