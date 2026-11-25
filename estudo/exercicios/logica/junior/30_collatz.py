"""
Logica junior 30 — Passos de Collatz

Par divide por 2. Impar vira 3n+1. Conte os passos ate chegar em 1. collatz(1) vale 0. n menor que 1 levanta ValueError.

Como testar:
    python3 logica/junior/30_collatz.py
"""

def collatz(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = collatz(1)
    _verificar(veio == 0, f"collatz(1) -> 0, veio {veio!r}", falhas)
    veio = collatz(2)
    _verificar(veio == 1, f"collatz(2) -> 1, veio {veio!r}", falhas)
    veio = collatz(3)
    _verificar(veio == 7, f"collatz(3) -> 7, veio {veio!r}", falhas)
    veio = collatz(6)
    _verificar(veio == 8, f"collatz(6) -> 8, veio {veio!r}", falhas)
    try:
        collatz(0)
        _verificar(False, "collatz(0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "collatz(0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

