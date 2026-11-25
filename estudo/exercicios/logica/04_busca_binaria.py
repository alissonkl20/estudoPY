"""
Exercicio 04 — Busca binaria

A lista ja vem ordenada, do menor para o maior, e pode ter repetidos.
Nao use list.index nem o operador `in` na lista inteira: corte o intervalo no meio.

Implemente indice(lista, alvo) -> int.

- devolve o menor indice em que alvo aparece
- se nao existir, devolve -1
- lista vazia devolve -1

Como testar:
    python3 logica/04_busca_binaria.py
"""


def indice(lista: list[int], alvo: int) -> int:
    # seu codigo aqui
    return -1


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(indice([], 1) == -1, "lista vazia", falhas)
    _verificar(indice([1, 3, 5, 7, 9], 7) == 3, "alvo no meio-direita", falhas)
    _verificar(indice([1, 3, 5, 7, 9], 1) == 0, "primeiro elemento", falhas)
    _verificar(indice([1, 3, 5, 7, 9], 9) == 4, "ultimo elemento", falhas)
    _verificar(indice([1, 3, 5, 7, 9], 4) == -1, "ausente", falhas)
    _verificar(indice([2, 2, 2, 2], 2) == 0, "todos iguais, menor indice", falhas)
    _verificar(indice([1, 2, 2, 2, 3], 2) == 1, "repetido no meio", falhas)
    _verificar(indice([1, 2, 2, 2, 3], 3) == 4, "alvo depois dos repetidos", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
