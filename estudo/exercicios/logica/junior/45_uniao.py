"""
Logica junior 45 — Uniao

Junte as duas listas sem repetir. Primeiro os da primeira, depois o que so existe na segunda.

Como testar:
    python3 logica/junior/45_uniao.py
"""

def uniao(a: list, b: list) -> list:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = uniao([1, 2], [2, 3])
    _verificar(veio == [1, 2, 3], f"uniao([1, 2], [2, 3]) -> [1, 2, 3], veio {veio!r}", falhas)
    veio = uniao([], [1, 1])
    _verificar(veio == [1], f"uniao([], [1, 1]) -> [1], veio {veio!r}", falhas)
    veio = uniao([2, 2], [])
    _verificar(veio == [2], f"uniao([2, 2], []) -> [2], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

