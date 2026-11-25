"""
Logica pleno 78 — K menores distintos

Devolva ate k menores valores distintos, em ordem. Se houver menos, devolva os que existirem. k menor que 1 levanta ValueError.

Como testar:
    python3 logica/pleno/78_k_menores.py
"""

def k_menores(nums: list[int], k: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = k_menores([4, 1, 3, 1, 2], 2)
    _verificar(veio == [1, 2], f"k_menores([4, 1, 3, 1, 2], 2) -> [1, 2], veio {veio!r}", falhas)
    veio = k_menores([5], 3)
    _verificar(veio == [5], f"k_menores([5], 3) -> [5], veio {veio!r}", falhas)
    veio = k_menores([], 1)
    _verificar(veio == [], f"k_menores([], 1) -> [], veio {veio!r}", falhas)
    try:
        k_menores([1], 0)
        _verificar(False, "k_menores([1], 0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "k_menores([1], 0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

