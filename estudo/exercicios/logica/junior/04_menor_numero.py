"""
Logica junior 04 — Menor numero

Devolva o menor inteiro. Lista vazia levanta ValueError.

Como testar:
    python3 logica/junior/04_menor_numero.py
"""

def menor_numero(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = menor_numero([1, 7, 3])
    _verificar(veio == 1, f"menor_numero([1, 7, 3]) -> 1, veio {veio!r}", falhas)
    veio = menor_numero([-5, -1, -8])
    _verificar(veio == -8, f"menor_numero([-5, -1, -8]) -> -8, veio {veio!r}", falhas)
    veio = menor_numero([4])
    _verificar(veio == 4, f"menor_numero([4]) -> 4, veio {veio!r}", falhas)
    try:
        menor_numero([])
        _verificar(False, "menor_numero([]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "menor_numero([]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

