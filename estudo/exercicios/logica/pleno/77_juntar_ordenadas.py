"""
Logica pleno 77 — Juntar listas ordenadas

As duas listas ja vem do menor para o maior. Devolva uma so, tambem ordenada.

Como testar:
    python3 logica/pleno/77_juntar_ordenadas.py
"""

def juntar_ordenadas(a: list[int], b: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = juntar_ordenadas([1, 3, 5], [2, 4])
    _verificar(veio == [1, 2, 3, 4, 5], f"juntar_ordenadas([1, 3, 5], [2, 4]) -> [1, 2, 3, 4, 5], veio {veio!r}", falhas)
    veio = juntar_ordenadas([], [1])
    _verificar(veio == [1], f"juntar_ordenadas([], [1]) -> [1], veio {veio!r}", falhas)
    veio = juntar_ordenadas([], [])
    _verificar(veio == [], f"juntar_ordenadas([], []) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

