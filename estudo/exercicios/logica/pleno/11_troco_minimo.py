"""
Logica pleno 11 — Troco minimo

Use cada moeda quantas vezes quiser. Devolva a menor quantidade. Se for impossivel, -1. Valor 0 vale 0.

Como testar:
    python3 logica/pleno/11_troco_minimo.py
"""

def troco_minimo(moedas: list[int], valor: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = troco_minimo([1, 2, 5], 11)
    _verificar(veio == 3, f"troco_minimo([1, 2, 5], 11) -> 3, veio {veio!r}", falhas)
    veio = troco_minimo([2], 3)
    _verificar(veio == -1, f"troco_minimo([2], 3) -> -1, veio {veio!r}", falhas)
    veio = troco_minimo([1], 0)
    _verificar(veio == 0, f"troco_minimo([1], 0) -> 0, veio {veio!r}", falhas)
    veio = troco_minimo([], 1)
    _verificar(veio == -1, f"troco_minimo([], 1) -> -1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

