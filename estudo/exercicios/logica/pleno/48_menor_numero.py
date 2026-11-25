"""
Logica pleno 48 — Menor numero removendo digitos

Apague k digitos para formar o menor numero, sem zero a esquerda, exceto o proprio 0. k maior que o tamanho levanta ValueError.

Como testar:
    python3 logica/pleno/48_menor_numero.py
"""

def menor_numero(numero: str, k: int) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = menor_numero('1432219', 3)
    _verificar(veio == '1219', f"menor_numero('1432219', 3) -> '1219', veio {veio!r}", falhas)
    veio = menor_numero('10200', 1)
    _verificar(veio == '200', f"menor_numero('10200', 1) -> '200', veio {veio!r}", falhas)
    veio = menor_numero('10', 2)
    _verificar(veio == '0', f"menor_numero('10', 2) -> '0', veio {veio!r}", falhas)
    try:
        menor_numero('10', 3)
        _verificar(False, "menor_numero('10', 3) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "menor_numero('10', 3) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

