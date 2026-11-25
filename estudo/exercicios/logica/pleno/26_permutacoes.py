"""
Logica pleno 26 — Permutacoes

Devolva as permutacoes em ordem lexicografica. A entrada nao tem repetidos. Lista vazia tem uma permutacao vazia.

Como testar:
    python3 logica/pleno/26_permutacoes.py
"""

def permutacoes(nums: list[int]) -> list[list[int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = permutacoes([1, 2])
    _verificar(veio == [[1, 2], [2, 1]], f"permutacoes([1, 2]) -> [[1, 2], [2, 1]], veio {veio!r}", falhas)
    veio = permutacoes([1])
    _verificar(veio == [[1]], f"permutacoes([1]) -> [[1]], veio {veio!r}", falhas)
    veio = permutacoes([])
    _verificar(veio == [[]], f"permutacoes([]) -> [[]], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

