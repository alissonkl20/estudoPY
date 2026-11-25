"""
Logica pleno 27 — Combinacoes

Escolha k numeros distintos de 1 ate n, em ordem. k igual a 0 devolve [[]]. k fora de 0..n levanta ValueError.

Como testar:
    python3 logica/pleno/27_combinacoes.py
"""

def combinacoes(n: int, k: int) -> list[list[int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = combinacoes(4, 2)
    _verificar(veio == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], f"combinacoes(4, 2) -> [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], veio {veio!r}", falhas)
    veio = combinacoes(3, 0)
    _verificar(veio == [[]], f"combinacoes(3, 0) -> [[]], veio {veio!r}", falhas)
    veio = combinacoes(3, 1)
    _verificar(veio == [[1], [2], [3]], f"combinacoes(3, 1) -> [[1], [2], [3]], veio {veio!r}", falhas)
    try:
        combinacoes(3, 4)
        _verificar(False, "combinacoes(3, 4) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "combinacoes(3, 4) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

