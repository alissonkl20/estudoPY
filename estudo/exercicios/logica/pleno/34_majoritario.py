"""
Logica pleno 34 — Elemento majoritario

Devolva o valor que aparece mais da metade das vezes. Se ninguem aparecer tanto, levante ValueError.

Como testar:
    python3 logica/pleno/34_majoritario.py
"""

def majoritario(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = majoritario([3, 2, 3])
    _verificar(veio == 3, f"majoritario([3, 2, 3]) -> 3, veio {veio!r}", falhas)
    veio = majoritario([6, 5, 5])
    _verificar(veio == 5, f"majoritario([6, 5, 5]) -> 5, veio {veio!r}", falhas)
    veio = majoritario([1])
    _verificar(veio == 1, f"majoritario([1]) -> 1, veio {veio!r}", falhas)
    try:
        majoritario([1, 2])
        _verificar(False, "majoritario([1, 2]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "majoritario([1, 2]) levanta ValueError", falhas)
    try:
        majoritario([])
        _verificar(False, "majoritario([]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "majoritario([]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

