"""
Logica pleno 63 — Avaliar polinomio

coefs[i] multiplica x elevado a i. Lista vazia vale 0.

Como testar:
    python3 logica/pleno/63_polinomio.py
"""

def polinomio(coefs: list[int], x: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = polinomio([1, 2, 3], 2)
    _verificar(veio == 17, f"polinomio([1, 2, 3], 2) -> 17, veio {veio!r}", falhas)
    veio = polinomio([5], 9)
    _verificar(veio == 5, f"polinomio([5], 9) -> 5, veio {veio!r}", falhas)
    veio = polinomio([], 4)
    _verificar(veio == 0, f"polinomio([], 4) -> 0, veio {veio!r}", falhas)
    veio = polinomio([1, 0, 1], -1)
    _verificar(veio == 2, f"polinomio([1, 0, 1], -1) -> 2, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

