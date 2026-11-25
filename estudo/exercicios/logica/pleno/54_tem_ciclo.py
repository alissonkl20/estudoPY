"""
Logica pleno 54 — Ciclo dirigido

n nos de 0 a n-1. Cada par (u, v) e uma aresta de u para v. Verdadeiro se houver ciclo.

Como testar:
    python3 logica/pleno/54_tem_ciclo.py
"""

def tem_ciclo(n: int, arestas: list[tuple[int, int]]) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = tem_ciclo(2, [(0, 1), (1, 0)])
    _verificar(veio == True, f"tem_ciclo(2, [(0, 1), (1, 0)]) -> True, veio {veio!r}", falhas)
    veio = tem_ciclo(2, [(0, 1)])
    _verificar(veio == False, f"tem_ciclo(2, [(0, 1)]) -> False, veio {veio!r}", falhas)
    veio = tem_ciclo(1, [])
    _verificar(veio == False, f"tem_ciclo(1, []) -> False, veio {veio!r}", falhas)
    veio = tem_ciclo(3, [(0, 1), (1, 2), (2, 1)])
    _verificar(veio == True, f"tem_ciclo(3, [(0, 1), (1, 2), (2, 1)]) -> True, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

