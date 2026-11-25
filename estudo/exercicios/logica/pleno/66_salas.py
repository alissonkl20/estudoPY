"""
Logica pleno 66 — Salas necessarias

Cada reserva e [inicio, fim), fim exclusivo. Encostar nao exige outra sala. fim menor ou igual a inicio levanta ValueError. Lista vazia vale 0.

Como testar:
    python3 logica/pleno/66_salas.py
"""

def salas(reservas: list[tuple[int, int]]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = salas([(0, 30), (5, 10), (15, 20)])
    _verificar(veio == 2, f"salas([(0, 30), (5, 10), (15, 20)]) -> 2, veio {veio!r}", falhas)
    veio = salas([(1, 2), (2, 3)])
    _verificar(veio == 1, f"salas([(1, 2), (2, 3)]) -> 1, veio {veio!r}", falhas)
    veio = salas([])
    _verificar(veio == 0, f"salas([]) -> 0, veio {veio!r}", falhas)
    try:
        salas([(1, 1)])
        _verificar(False, "salas([(1, 1)]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "salas([(1, 1)]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

