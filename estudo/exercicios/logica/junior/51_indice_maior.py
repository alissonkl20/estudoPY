"""
Logica junior 51 — Indice do maior

Devolva o primeiro indice do maior valor. Lista vazia levanta ValueError.

Como testar:
    python3 logica/junior/51_indice_maior.py
"""

def indice_maior(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = indice_maior([1, 3, 3])
    _verificar(veio == 1, f"indice_maior([1, 3, 3]) -> 1, veio {veio!r}", falhas)
    veio = indice_maior([-2, -5])
    _verificar(veio == 0, f"indice_maior([-2, -5]) -> 0, veio {veio!r}", falhas)
    veio = indice_maior([4])
    _verificar(veio == 0, f"indice_maior([4]) -> 0, veio {veio!r}", falhas)
    try:
        indice_maior([])
        _verificar(False, "indice_maior([]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "indice_maior([]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

