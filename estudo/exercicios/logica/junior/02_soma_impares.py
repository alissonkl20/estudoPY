"""
Logica junior 02 — Somar impares

Some os inteiros impares. Lista vazia vale 0.

Como testar:
    python3 logica/junior/02_soma_impares.py
"""

def soma_impares(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = soma_impares([1, 2, 3, 4])
    _verificar(veio == 4, f"soma_impares([1, 2, 3, 4]) -> 4, veio {veio!r}", falhas)
    veio = soma_impares([])
    _verificar(veio == 0, f"soma_impares([]) -> 0, veio {veio!r}", falhas)
    veio = soma_impares([2, 4])
    _verificar(veio == 0, f"soma_impares([2, 4]) -> 0, veio {veio!r}", falhas)
    veio = soma_impares([-3, 8, 5])
    _verificar(veio == 2, f"soma_impares([-3, 8, 5]) -> 2, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

