"""
Logica pleno 30 — Agua da chuva

Cada posicao e a altura de uma barra. Conte quanta agua fica presa entre elas. Lista vazia vale 0.

Como testar:
    python3 logica/pleno/30_agua_parada.py
"""

def agua_parada(alturas: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = agua_parada([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    _verificar(veio == 6, f"agua_parada([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) -> 6, veio {veio!r}", falhas)
    veio = agua_parada([1, 0, 1])
    _verificar(veio == 1, f"agua_parada([1, 0, 1]) -> 1, veio {veio!r}", falhas)
    veio = agua_parada([])
    _verificar(veio == 0, f"agua_parada([]) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

