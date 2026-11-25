"""
Logica junior 79 — Produto da lista

Multiplique os inteiros. Lista vazia vale 1, o elemento neutro da multiplicacao.

Como testar:
    python3 logica/junior/79_produto_lista.py
"""

def produto_lista(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = produto_lista([2, 3, 4])
    _verificar(veio == 24, f"produto_lista([2, 3, 4]) -> 24, veio {veio!r}", falhas)
    veio = produto_lista([])
    _verificar(veio == 1, f"produto_lista([]) -> 1, veio {veio!r}", falhas)
    veio = produto_lista([5, 0, 2])
    _verificar(veio == 0, f"produto_lista([5, 0, 2]) -> 0, veio {veio!r}", falhas)
    veio = produto_lista([-2, 3])
    _verificar(veio == -6, f"produto_lista([-2, 3]) -> -6, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

