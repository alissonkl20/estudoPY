"""
Logica pleno 19 — Mais frequentes

Devolva os k valores mais frequentes. Empate de frequencia desempata pelo valor menor. k menor que 1 levanta ValueError. Se k passar dos distintos, devolva todos.

Como testar:
    python3 logica/pleno/19_mais_frequentes.py
"""

def mais_frequentes(nums: list[int], k: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = mais_frequentes([1, 1, 1, 2, 2, 3], 2)
    _verificar(veio == [1, 2], f"mais_frequentes([1, 1, 1, 2, 2, 3], 2) -> [1, 2], veio {veio!r}", falhas)
    veio = mais_frequentes([4, 4, 3, 3], 2)
    _verificar(veio == [3, 4], f"mais_frequentes([4, 4, 3, 3], 2) -> [3, 4], veio {veio!r}", falhas)
    veio = mais_frequentes([4, 4, 3, 3], 1)
    _verificar(veio == [3], f"mais_frequentes([4, 4, 3, 3], 1) -> [3], veio {veio!r}", falhas)
    veio = mais_frequentes([1, 1, 2], 5)
    _verificar(veio == [1, 2], f"mais_frequentes([1, 1, 2], 5) -> [1, 2], veio {veio!r}", falhas)
    try:
        mais_frequentes([1], 0)
        _verificar(False, "mais_frequentes([1], 0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "mais_frequentes([1], 0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

