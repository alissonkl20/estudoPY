"""
Exercicio 09 — Par que soma o alvo

Ache dois indices diferentes cuja soma dos valores seja o alvo.
Um dicionario guarda o valor ja visto e o indice dele.

Implemente indices_que_somam(nums, alvo) -> tuple[int, int] | None.

- i vem antes de j
- se houver varios pares, escolha o de menor j
- se esse j formar par com mais de um i, escolha o menor i
- se nao houver par, devolve None
- o mesmo indice nao pode ser usado duas vezes

Como testar:
    python3 logica/09_par_soma.py
"""


def indices_que_somam(nums: list[int], alvo: int) -> tuple[int, int] | None:
    # seu codigo aqui
    return None


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(indices_que_somam([2, 7, 11, 15], 9) == (0, 1), "par classico", falhas)
    _verificar(indices_que_somam([3, 3], 6) == (0, 1), "valores iguais", falhas)
    _verificar(indices_que_somam([1, 2, 3], 7) is None, "sem par", falhas)
    _verificar(indices_que_somam([0, 4, 3, 0], 0) == (0, 3), "zeros nas pontas", falhas)
    _verificar(
        indices_que_somam([3, 1, 4, 2], 5) == (1, 2),
        "menor j vence o par que comeca antes",
        falhas,
    )
    _verificar(indices_que_somam([5], 10) is None, "um elemento nao soma com ele mesmo", falhas)
    _verificar(indices_que_somam([], 0) is None, "lista vazia", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
