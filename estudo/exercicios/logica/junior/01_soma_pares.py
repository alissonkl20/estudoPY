"""
Logica junior 01 — Somar pares

Some os inteiros pares. Lista vazia vale 0. Negativo par entra na soma.

Como testar:
    python3 logica/junior/01_soma_pares.py
"""

def soma_pares(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = soma_pares([1, 2, 3, 4])
    _verificar(veio == 6, f"soma_pares([1, 2, 3, 4]) -> 6, veio {veio!r}", falhas)
    veio = soma_pares([])
    _verificar(veio == 0, f"soma_pares([]) -> 0, veio {veio!r}", falhas)
    veio = soma_pares([1, 3, 5])
    _verificar(veio == 0, f"soma_pares([1, 3, 5]) -> 0, veio {veio!r}", falhas)
    veio = soma_pares([-2, 4, 7])
    _verificar(veio == 2, f"soma_pares([-2, 4, 7]) -> 2, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

