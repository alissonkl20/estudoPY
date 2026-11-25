"""
Logica pleno 55 — Busca em lista rotacionada

A lista ordenada foi girada e nao tem repetidos. Devolva o indice do alvo, ou -1.

Como testar:
    python3 logica/pleno/55_busca_rotacionada.py
"""

def busca_rotacionada(nums: list[int], alvo: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = busca_rotacionada([4, 5, 6, 7, 0, 1, 2], 0)
    _verificar(veio == 4, f"busca_rotacionada([4, 5, 6, 7, 0, 1, 2], 0) -> 4, veio {veio!r}", falhas)
    veio = busca_rotacionada([4, 5, 6, 7, 0, 1, 2], 3)
    _verificar(veio == -1, f"busca_rotacionada([4, 5, 6, 7, 0, 1, 2], 3) -> -1, veio {veio!r}", falhas)
    veio = busca_rotacionada([1], 1)
    _verificar(veio == 0, f"busca_rotacionada([1], 1) -> 0, veio {veio!r}", falhas)
    veio = busca_rotacionada([], 1)
    _verificar(veio == -1, f"busca_rotacionada([], 1) -> -1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

