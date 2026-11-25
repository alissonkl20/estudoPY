"""
Logica pleno 20 — Kesimo maior distinto

k comeca em 1. Repetido conta uma vez. k fora da quantidade de distintos levanta ValueError.

Como testar:
    python3 logica/pleno/20_kesimo_maior.py
"""

def kesimo_maior(nums: list[int], k: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = kesimo_maior([3, 2, 3, 1], 1)
    _verificar(veio == 3, f"kesimo_maior([3, 2, 3, 1], 1) -> 3, veio {veio!r}", falhas)
    veio = kesimo_maior([3, 2, 3, 1], 2)
    _verificar(veio == 2, f"kesimo_maior([3, 2, 3, 1], 2) -> 2, veio {veio!r}", falhas)
    veio = kesimo_maior([5], 1)
    _verificar(veio == 5, f"kesimo_maior([5], 1) -> 5, veio {veio!r}", falhas)
    try:
        kesimo_maior([1, 2], 3)
        _verificar(False, "kesimo_maior([1, 2], 3) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "kesimo_maior([1, 2], 3) levanta ValueError", falhas)
    try:
        kesimo_maior([1], 0)
        _verificar(False, "kesimo_maior([1], 0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "kesimo_maior([1], 0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

