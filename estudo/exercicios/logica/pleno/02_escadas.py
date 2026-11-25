"""
Logica pleno 02 — Escadas

Cada degrau sobe 1 ou 2. Conte as formas de chegar em n. n menor que 1 levanta ValueError.

Como testar:
    python3 logica/pleno/02_escadas.py
"""

def escadas(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = escadas(1)
    _verificar(veio == 1, f"escadas(1) -> 1, veio {veio!r}", falhas)
    veio = escadas(2)
    _verificar(veio == 2, f"escadas(2) -> 2, veio {veio!r}", falhas)
    veio = escadas(3)
    _verificar(veio == 3, f"escadas(3) -> 3, veio {veio!r}", falhas)
    veio = escadas(5)
    _verificar(veio == 8, f"escadas(5) -> 8, veio {veio!r}", falhas)
    try:
        escadas(0)
        _verificar(False, "escadas(0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "escadas(0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

