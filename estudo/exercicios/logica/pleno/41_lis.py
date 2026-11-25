"""
Logica pleno 41 — Subsequencia crescente

Devolva o tamanho da maior subsequencia estritamente crescente. Lista vazia vale 0.

Como testar:
    python3 logica/pleno/41_lis.py
"""

def lis(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = lis([10, 9, 2, 5, 3, 7, 101, 18])
    _verificar(veio == 4, f"lis([10, 9, 2, 5, 3, 7, 101, 18]) -> 4, veio {veio!r}", falhas)
    veio = lis([])
    _verificar(veio == 0, f"lis([]) -> 0, veio {veio!r}", falhas)
    veio = lis([1, 2, 3])
    _verificar(veio == 3, f"lis([1, 2, 3]) -> 3, veio {veio!r}", falhas)
    veio = lis([3, 2, 1])
    _verificar(veio == 1, f"lis([3, 2, 1]) -> 1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

