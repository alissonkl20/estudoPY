"""
Logica junior 36 — Conceito da nota

A desde 9, B desde 7, C desde 5, D desde 3, F abaixo disso. Nota fora de 0 a 10 levanta ValueError. bool nao vale.

Como testar:
    python3 logica/junior/36_conceito.py
"""

def conceito(nota: float) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = conceito(9)
    _verificar(veio == 'A', f"conceito(9) -> 'A', veio {veio!r}", falhas)
    veio = conceito(8.9)
    _verificar(veio == 'B', f"conceito(8.9) -> 'B', veio {veio!r}", falhas)
    veio = conceito(7)
    _verificar(veio == 'B', f"conceito(7) -> 'B', veio {veio!r}", falhas)
    veio = conceito(5)
    _verificar(veio == 'C', f"conceito(5) -> 'C', veio {veio!r}", falhas)
    veio = conceito(3)
    _verificar(veio == 'D', f"conceito(3) -> 'D', veio {veio!r}", falhas)
    veio = conceito(2)
    _verificar(veio == 'F', f"conceito(2) -> 'F', veio {veio!r}", falhas)
    veio = conceito(0)
    _verificar(veio == 'F', f"conceito(0) -> 'F', veio {veio!r}", falhas)
    try:
        conceito(11)
        _verificar(False, "conceito(11) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "conceito(11) levanta ValueError", falhas)
    try:
        conceito(-1)
        _verificar(False, "conceito(-1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "conceito(-1) levanta ValueError", falhas)
    try:
        conceito(True)
        _verificar(False, "conceito(True) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "conceito(True) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

