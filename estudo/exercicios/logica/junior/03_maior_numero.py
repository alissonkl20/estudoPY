"""
Logica junior 03 — Maior numero

Devolva o maior inteiro. Lista vazia levanta ValueError. Empate fica com o proprio valor.

Como testar:
    python3 logica/junior/03_maior_numero.py
"""

def maior_numero(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = maior_numero([1, 7, 3])
    _verificar(veio == 7, f"maior_numero([1, 7, 3]) -> 7, veio {veio!r}", falhas)
    veio = maior_numero([-5, -1, -8])
    _verificar(veio == -1, f"maior_numero([-5, -1, -8]) -> -1, veio {veio!r}", falhas)
    veio = maior_numero([4, 4])
    _verificar(veio == 4, f"maior_numero([4, 4]) -> 4, veio {veio!r}", falhas)
    try:
        maior_numero([])
        _verificar(False, "maior_numero([]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "maior_numero([]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

