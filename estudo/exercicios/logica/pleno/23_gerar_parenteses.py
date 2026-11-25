"""
Logica pleno 23 — Gerar parenteses

Gere todas as sequencias com n pares, em ordem. n menor que 1 levanta ValueError.

Como testar:
    python3 logica/pleno/23_gerar_parenteses.py
"""

def gerar_parenteses(n: int) -> list[str]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = gerar_parenteses(1)
    _verificar(veio == ['()'], f"gerar_parenteses(1) -> ['()'], veio {veio!r}", falhas)
    veio = gerar_parenteses(2)
    _verificar(veio == ['(())', '()()'], f"gerar_parenteses(2) -> ['(())', '()()'], veio {veio!r}", falhas)
    veio = gerar_parenteses(3)
    _verificar(veio == ['((()))', '(()())', '(())()', '()(())', '()()()'], f"gerar_parenteses(3) -> ['((()))', '(()())', '(())()', '()(())', '()()()'], veio {veio!r}", falhas)
    try:
        gerar_parenteses(0)
        _verificar(False, "gerar_parenteses(0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "gerar_parenteses(0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

