"""
Logica junior 67 — Diagonal principal

Some a diagonal de uma matriz quadrada. Matriz vazia ou que nao e quadrada levanta ValueError.

Como testar:
    python3 logica/junior/67_diagonal.py
"""

def diagonal(matriz: list[list[int]]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = diagonal([[1, 2], [3, 4]])
    _verificar(veio == 5, f"diagonal([[1, 2], [3, 4]]) -> 5, veio {veio!r}", falhas)
    veio = diagonal([[7]])
    _verificar(veio == 7, f"diagonal([[7]]) -> 7, veio {veio!r}", falhas)
    try:
        diagonal([])
        _verificar(False, "diagonal([]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "diagonal([]) levanta ValueError", falhas)
    try:
        diagonal([[1, 2]])
        _verificar(False, "diagonal([[1, 2]]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "diagonal([[1, 2]]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

