"""
Logica pleno 53 — Custo da arvore minima

n nos de 0 a n-1. Cada aresta e (u, v, peso). Devolva o custo da arvore que liga todos. Se ficar separado, -1. Um no so vale 0.

Como testar:
    python3 logica/pleno/53_custo_mst.py
"""

def custo_mst(n: int, arestas: list[tuple[int, int, int]]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = custo_mst(3, [(0, 1, 1), (1, 2, 2), (0, 2, 10)])
    _verificar(veio == 3, f"custo_mst(3, [(0, 1, 1), (1, 2, 2), (0, 2, 10)]) -> 3, veio {veio!r}", falhas)
    veio = custo_mst(2, [])
    _verificar(veio == -1, f"custo_mst(2, []) -> -1, veio {veio!r}", falhas)
    veio = custo_mst(1, [])
    _verificar(veio == 0, f"custo_mst(1, []) -> 0, veio {veio!r}", falhas)
    try:
        custo_mst(0, [])
        _verificar(False, "custo_mst(0, []) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "custo_mst(0, []) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

