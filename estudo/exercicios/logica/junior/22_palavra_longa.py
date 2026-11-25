"""
Logica junior 22 — Palavra mais longa

Devolva a primeira palavra de maior tamanho. Texto sem palavra levanta ValueError.

Como testar:
    python3 logica/junior/22_palavra_longa.py
"""

def palavra_longa(texto: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = palavra_longa('o gato')
    _verificar(veio == 'gato', f"palavra_longa('o gato') -> 'gato', veio {veio!r}", falhas)
    veio = palavra_longa('aa bb cc')
    _verificar(veio == 'aa', f"palavra_longa('aa bb cc') -> 'aa', veio {veio!r}", falhas)
    veio = palavra_longa('  sol  lua  ')
    _verificar(veio == 'sol', f"palavra_longa('  sol  lua  ') -> 'sol', veio {veio!r}", falhas)
    try:
        palavra_longa('')
        _verificar(False, "palavra_longa('') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "palavra_longa('') levanta ValueError", falhas)
    try:
        palavra_longa('   ')
        _verificar(False, "palavra_longa('   ') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "palavra_longa('   ') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

