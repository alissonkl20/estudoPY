"""
Logica junior 09 — Fibonacci

A sequencia comeca 1, 1, 2, 3, 5. fibonacci(1) vale 1. n menor que 1 levanta ValueError.

Como testar:
    python3 logica/junior/09_fibonacci.py
"""

def fibonacci(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = fibonacci(1)
    _verificar(veio == 1, f"fibonacci(1) -> 1, veio {veio!r}", falhas)
    veio = fibonacci(2)
    _verificar(veio == 1, f"fibonacci(2) -> 1, veio {veio!r}", falhas)
    veio = fibonacci(6)
    _verificar(veio == 8, f"fibonacci(6) -> 8, veio {veio!r}", falhas)
    veio = fibonacci(8)
    _verificar(veio == 21, f"fibonacci(8) -> 21, veio {veio!r}", falhas)
    try:
        fibonacci(0)
        _verificar(False, "fibonacci(0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "fibonacci(0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

