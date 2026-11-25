"""
Logica junior 64 — Comprimir texto

Agrupe letras repetidas em sequencia. "aaabbc" vira [["a", 3], ["b", 2], ["c", 1]].

Como testar:
    python3 logica/junior/64_comprimir.py
"""

def comprimir(texto: str) -> list[list]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = comprimir('aaabbc')
    _verificar(veio == [['a', 3], ['b', 2], ['c', 1]], f"comprimir('aaabbc') -> [['a', 3], ['b', 2], ['c', 1]], veio {veio!r}", falhas)
    veio = comprimir('')
    _verificar(veio == [], f"comprimir('') -> [], veio {veio!r}", falhas)
    veio = comprimir('abc')
    _verificar(veio == [['a', 1], ['b', 1], ['c', 1]], f"comprimir('abc') -> [['a', 1], ['b', 1], ['c', 1]], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

