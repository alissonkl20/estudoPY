"""
Logica junior 17 — Limitar um numero

Se n estiver abaixo de inicio, devolva inicio. Se estiver acima de fim, devolva fim. inicio maior que fim levanta ValueError.

Como testar:
    python3 logica/junior/17_limitar.py
"""

def limitar(n: int, inicio: int, fim: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = limitar(5, 1, 3)
    _verificar(veio == 3, f"limitar(5, 1, 3) -> 3, veio {veio!r}", falhas)
    veio = limitar(0, 1, 3)
    _verificar(veio == 1, f"limitar(0, 1, 3) -> 1, veio {veio!r}", falhas)
    veio = limitar(2, 1, 3)
    _verificar(veio == 2, f"limitar(2, 1, 3) -> 2, veio {veio!r}", falhas)
    veio = limitar(-4, -2, -1)
    _verificar(veio == -2, f"limitar(-4, -2, -1) -> -2, veio {veio!r}", falhas)
    try:
        limitar(1, 5, 1)
        _verificar(False, "limitar(1, 5, 1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "limitar(1, 5, 1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

