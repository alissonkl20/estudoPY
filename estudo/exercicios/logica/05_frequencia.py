"""
Exercicio 05 — Segundo maior e mais frequente

Contar e comparar, sem ordenar a lista inteira se nao precisar.

Implemente segundo_maior(nums) -> int | None e mais_frequente(itens).

segundo_maior:
- olha os valores distintos
- [5, 5, 4] devolve 4
- menos de dois valores distintos devolve None
- negativos entram na conta

mais_frequente:
- lista vazia levanta ValueError
- em empate de contagem, devolve o item que aparece primeiro
- [1, 2, 2, 1] devolve 1

Como testar:
    python3 logica/05_frequencia.py
"""


def segundo_maior(nums: list[int]) -> int | None:
    # seu codigo aqui
    return None


def mais_frequente(itens: list):
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

    _verificar(segundo_maior([5, 5, 4]) == 4, "repetido no topo", falhas)
    _verificar(segundo_maior([3, 1, 2]) == 2, "tres distintos", falhas)
    _verificar(segundo_maior([-1, -5, -1]) == -5, "negativos", falhas)
    _verificar(segundo_maior([7]) is None, "um valor so", falhas)
    _verificar(segundo_maior([]) is None, "lista vazia", falhas)
    _verificar(segundo_maior([8, 8, 8]) is None, "todos iguais", falhas)

    _verificar(mais_frequente([1, 2, 2, 1]) == 1, "empate fica com o primeiro", falhas)
    _verificar(mais_frequente(["a", "b", "b"]) == "b", "vencedor unico", falhas)
    _verificar(mais_frequente([True, True, False]) is True, "bool tambem e item", falhas)

    try:
        mais_frequente([])
        _verificar(False, "lista vazia deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "lista vazia levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
