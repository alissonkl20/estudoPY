"""
Logica junior 43 — Intersecao

Devolva os valores que estao nas duas listas, na ordem da primeira, sem repetir.

Como testar:
    python3 logica/junior/43_intersecao.py
"""

def intersecao(a: list, b: list) -> list:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = intersecao([1, 2, 2, 3], [2, 4])
    _verificar(veio == [2], f"intersecao([1, 2, 2, 3], [2, 4]) -> [2], veio {veio!r}", falhas)
    veio = intersecao([1, 2], [3])
    _verificar(veio == [], f"intersecao([1, 2], [3]) -> [], veio {veio!r}", falhas)
    veio = intersecao([], [1])
    _verificar(veio == [], f"intersecao([], [1]) -> [], veio {veio!r}", falhas)
    veio = intersecao([3, 1, 3], [1, 3])
    _verificar(veio == [3, 1], f"intersecao([3, 1, 3], [1, 3]) -> [3, 1], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

