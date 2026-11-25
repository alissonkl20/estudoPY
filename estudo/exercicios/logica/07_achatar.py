"""
Exercicio 07 — Achatar lista aninhada

So lista e container. Texto, tupla e numero sao folhas: nao percorra os caracteres
de uma string.

Implemente achatar(valor) -> list, com recursao.

achatar([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
achatar(["ab", ["c"]]) == ["ab", "c"]
achatar(1) == [1]

Como testar:
    python3 logica/07_achatar.py
"""


def achatar(valor) -> list:
    # seu codigo aqui
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(achatar([]) == [], "lista vazia", falhas)
    _verificar(achatar(1) == [1], "folha numerica", falhas)
    _verificar(
        achatar([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6],
        "tres niveis",
        falhas,
    )
    _verificar(achatar([[], [1], []]) == [1], "listas vazias no meio", falhas)
    _verificar(achatar(["ab", ["c"]]) == ["ab", "c"], "string nao e percorrida", falhas)
    _verificar(achatar([(1, 2), [3]]) == [(1, 2), 3], "tupla e folha", falhas)
    _verificar(achatar([[[]]]) == [], "so cascas vazias", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
