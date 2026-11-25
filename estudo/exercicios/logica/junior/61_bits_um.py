"""
Logica junior 61 — Bits ligados

Conte quantos bits 1 existem na representacao binaria. Negativo levanta ValueError. 0 vale 0.

Como testar:
    python3 logica/junior/61_bits_um.py
"""

def bits_um(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = bits_um(0)
    _verificar(veio == 0, f"bits_um(0) -> 0, veio {veio!r}", falhas)
    veio = bits_um(7)
    _verificar(veio == 3, f"bits_um(7) -> 3, veio {veio!r}", falhas)
    veio = bits_um(8)
    _verificar(veio == 1, f"bits_um(8) -> 1, veio {veio!r}", falhas)
    veio = bits_um(9)
    _verificar(veio == 2, f"bits_um(9) -> 2, veio {veio!r}", falhas)
    try:
        bits_um(-1)
        _verificar(False, "bits_um(-1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "bits_um(-1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

