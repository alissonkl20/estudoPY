"""
Exercicio 08 — Maior soma de uma janela

Ache a maior soma de k numeros consecutivos, percorrendo a lista uma vez.
Quando a janela anda, tire o numero que saiu e some o que entrou.

Implemente maior_soma(nums, k) -> int.

- k < 1 levanta ValueError
- k maior que o tamanho da lista levanta ValueError
- numeros negativos entram na soma

Como testar:
    python3 logica/08_maior_soma.py
"""


def maior_soma(nums: list[int], k: int) -> int:
    # seu codigo aqui
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(maior_soma([1, 2, 3, 4], 2) == 7, "janela no fim", falhas)
    _verificar(maior_soma([5, 1, 3, 2], 2) == 6, "janela no inicio", falhas)
    _verificar(maior_soma([5], 1) == 5, "janela de um", falhas)
    _verificar(maior_soma([-1, -2, -3], 2) == -3, "todos negativos", falhas)
    _verificar(maior_soma([1, -4, 3, 3], 2) == 6, "janela no meio", falhas)
    _verificar(maior_soma([4, 2, 1], 3) == 7, "janela do tamanho da lista", falhas)

    try:
        maior_soma([1, 2], 0)
        _verificar(False, "k 0 deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "k 0 levanta ValueError", falhas)

    try:
        maior_soma([1, 2], 3)
        _verificar(False, "k grande demais deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "k grande demais levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
