"""
Logica junior 44 — Diferenca

Devolva o que esta na primeira lista e nao esta na segunda, sem repetir, na ordem da primeira.

Como testar:
    python3 logica/junior/44_diferenca.py
"""

def diferenca(a: list, b: list) -> list:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = diferenca([1, 2, 2, 3], [2])
    _verificar(veio == [1, 3], f"diferenca([1, 2, 2, 3], [2]) -> [1, 3], veio {veio!r}", falhas)
    veio = diferenca([1, 2], [])
    _verificar(veio == [1, 2], f"diferenca([1, 2], []) -> [1, 2], veio {veio!r}", falhas)
    veio = diferenca([1], [1])
    _verificar(veio == [], f"diferenca([1], [1]) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

