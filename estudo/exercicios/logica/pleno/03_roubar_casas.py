"""
Logica pleno 03 — Roubar casas

Nao roube duas casas vizinhas. Devolva o maior valor. Lista vazia vale 0.

Como testar:
    python3 logica/pleno/03_roubar_casas.py
"""

def roubar_casas(casas: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = roubar_casas([1, 2, 3, 1])
    _verificar(veio == 4, f"roubar_casas([1, 2, 3, 1]) -> 4, veio {veio!r}", falhas)
    veio = roubar_casas([2, 7, 9, 3, 1])
    _verificar(veio == 12, f"roubar_casas([2, 7, 9, 3, 1]) -> 12, veio {veio!r}", falhas)
    veio = roubar_casas([])
    _verificar(veio == 0, f"roubar_casas([]) -> 0, veio {veio!r}", falhas)
    veio = roubar_casas([5])
    _verificar(veio == 5, f"roubar_casas([5]) -> 5, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

