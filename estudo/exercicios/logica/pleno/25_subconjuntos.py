"""
Logica pleno 25 — Subconjuntos

Devolva todos os subconjuntos. Cada um vem ordenado. A lista vai do menor para o maior, e empate de tamanho fica em ordem lexicografica. A entrada nao tem repetidos.

Como testar:
    python3 logica/pleno/25_subconjuntos.py
"""

def subconjuntos(nums: list[int]) -> list[list[int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = subconjuntos([1, 2])
    _verificar(veio == [[], [1], [2], [1, 2]], f"subconjuntos([1, 2]) -> [[], [1], [2], [1, 2]], veio {veio!r}", falhas)
    veio = subconjuntos([])
    _verificar(veio == [[]], f"subconjuntos([]) -> [[]], veio {veio!r}", falhas)
    veio = subconjuntos([3])
    _verificar(veio == [[], [3]], f"subconjuntos([3]) -> [[], [3]], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

