"""
Logica pleno 36 — Saltos minimos

Cada valor e o alcance maximo. Devolva o minimo de saltos ate o fim. Se for impossivel, levante ValueError. Uma casa so vale 0.

Como testar:
    python3 logica/pleno/36_saltos_minimos.py
"""

def saltos_minimos(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = saltos_minimos([2, 3, 1, 1, 4])
    _verificar(veio == 2, f"saltos_minimos([2, 3, 1, 1, 4]) -> 2, veio {veio!r}", falhas)
    veio = saltos_minimos([0])
    _verificar(veio == 0, f"saltos_minimos([0]) -> 0, veio {veio!r}", falhas)
    veio = saltos_minimos([1, 0])
    _verificar(veio == 1, f"saltos_minimos([1, 0]) -> 1, veio {veio!r}", falhas)
    try:
        saltos_minimos([0, 1])
        _verificar(False, "saltos_minimos([0, 1]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "saltos_minimos([0, 1]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

