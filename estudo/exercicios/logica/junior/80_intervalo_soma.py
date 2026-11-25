"""
Logica junior 80 — Soma de um intervalo

Some os inteiros de inicio ate fim, inclusive. Se inicio for maior que fim, levante ValueError.

Como testar:
    python3 logica/junior/80_intervalo_soma.py
"""

def intervalo_soma(inicio: int, fim: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = intervalo_soma(1, 3)
    _verificar(veio == 6, f"intervalo_soma(1, 3) -> 6, veio {veio!r}", falhas)
    veio = intervalo_soma(3, 3)
    _verificar(veio == 3, f"intervalo_soma(3, 3) -> 3, veio {veio!r}", falhas)
    veio = intervalo_soma(-2, 1)
    _verificar(veio == -2, f"intervalo_soma(-2, 1) -> -2, veio {veio!r}", falhas)
    veio = intervalo_soma(0, 0)
    _verificar(veio == 0, f"intervalo_soma(0, 0) -> 0, veio {veio!r}", falhas)
    try:
        intervalo_soma(3, 1)
        _verificar(False, "intervalo_soma(3, 1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "intervalo_soma(3, 1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

