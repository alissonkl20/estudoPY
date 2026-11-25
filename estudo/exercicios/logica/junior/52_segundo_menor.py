"""
Logica junior 52 — Segundo menor

Olhe os valores distintos e devolva o segundo menor. Se houver menos de dois, devolva None.

Como testar:
    python3 logica/junior/52_segundo_menor.py
"""

def segundo_menor(nums: list[int]) -> int | None:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = segundo_menor([4, 1, 4, 2])
    _verificar(veio == 2, f"segundo_menor([4, 1, 4, 2]) -> 2, veio {veio!r}", falhas)
    veio = segundo_menor([5, 5])
    _verificar(veio == None, f"segundo_menor([5, 5]) -> None, veio {veio!r}", falhas)
    veio = segundo_menor([])
    _verificar(veio == None, f"segundo_menor([]) -> None, veio {veio!r}", falhas)
    veio = segundo_menor([3, 1])
    _verificar(veio == 3, f"segundo_menor([3, 1]) -> 3, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

