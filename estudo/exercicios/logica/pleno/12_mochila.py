"""
Logica pleno 12 — Mochila

Cada item entra no maximo uma vez. pesos e valores tem o mesmo tamanho. Capacidade 0 vale 0.

Como testar:
    python3 logica/pleno/12_mochila.py
"""

def mochila(pesos: list[int], valores: list[int], capacidade: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = mochila([1, 3, 4], [15, 20, 30], 4)
    _verificar(veio == 35, f"mochila([1, 3, 4], [15, 20, 30], 4) -> 35, veio {veio!r}", falhas)
    veio = mochila([], [], 5)
    _verificar(veio == 0, f"mochila([], [], 5) -> 0, veio {veio!r}", falhas)
    veio = mochila([2], [9], 0)
    _verificar(veio == 0, f"mochila([2], [9], 0) -> 0, veio {veio!r}", falhas)
    try:
        mochila([1], [1, 2], 3)
        _verificar(False, "mochila([1], [1, 2], 3) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "mochila([1], [1, 2], 3) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

