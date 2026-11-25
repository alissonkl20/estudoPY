"""
Logica junior 39 — Repetir texto

Repita o texto n vezes. n igual a 0 devolve vazio. n negativo ou bool levanta ValueError.

Como testar:
    python3 logica/junior/39_repetir_texto.py
"""

def repetir_texto(texto: str, n: int) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = repetir_texto('ab', 3)
    _verificar(veio == 'ababab', f"repetir_texto('ab', 3) -> 'ababab', veio {veio!r}", falhas)
    veio = repetir_texto('ab', 0)
    _verificar(veio == '', f"repetir_texto('ab', 0) -> '', veio {veio!r}", falhas)
    veio = repetir_texto('x', 1)
    _verificar(veio == 'x', f"repetir_texto('x', 1) -> 'x', veio {veio!r}", falhas)
    try:
        repetir_texto('ab', -1)
        _verificar(False, "repetir_texto('ab', -1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "repetir_texto('ab', -1) levanta ValueError", falhas)
    try:
        repetir_texto('ab', True)
        _verificar(False, "repetir_texto('ab', True) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "repetir_texto('ab', True) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

