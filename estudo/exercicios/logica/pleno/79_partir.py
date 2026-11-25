"""
Logica pleno 79 — Partir pelo pivo

Devolva tres listas, na ordem: menores, iguais e maiores. Dentro de cada uma, mantenha a ordem original.

Como testar:
    python3 logica/pleno/79_partir.py
"""

def partir(nums: list[int], pivo: int) -> tuple[list[int], list[int], list[int]]:
    return ()


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = partir([3, 1, 4, 2, 3], 3)
    _verificar(veio == ([1, 2], [3, 3], [4]), f"partir([3, 1, 4, 2, 3], 3) -> ([1, 2], [3, 3], [4]), veio {veio!r}", falhas)
    veio = partir([], 1)
    _verificar(veio == ([], [], []), f"partir([], 1) -> ([], [], []), veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

