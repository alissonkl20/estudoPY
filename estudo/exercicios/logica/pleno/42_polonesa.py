"""
Logica pleno 42 — Notacao polonesa

Tokens sao inteiros ou + - * /. A divisao trunca em direcao ao zero. Expressao invalida levanta ValueError.

Como testar:
    python3 logica/pleno/42_polonesa.py
"""

def polonesa(tokens: list[str]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = polonesa(['2', '1', '+', '3', '*'])
    _verificar(veio == 9, f"polonesa(['2', '1', '+', '3', '*']) -> 9, veio {veio!r}", falhas)
    veio = polonesa(['4', '13', '5', '/', '+'])
    _verificar(veio == 6, f"polonesa(['4', '13', '5', '/', '+']) -> 6, veio {veio!r}", falhas)
    veio = polonesa(['7', '-3', '/'])
    _verificar(veio == -2, f"polonesa(['7', '-3', '/']) -> -2, veio {veio!r}", falhas)
    try:
        polonesa(['2', '+'])
        _verificar(False, "polonesa(['2', '+']) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "polonesa(['2', '+']) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

