"""
Logica junior 65 — Expandir grupos

Cada grupo e [caractere, quantidade]. Quantidade menor que 1, ou caractere que nao tem tamanho 1, levanta ValueError.

Como testar:
    python3 logica/junior/65_expandir.py
"""

def expandir(partes: list) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = expandir([['a', 3], ['b', 2]])
    _verificar(veio == 'aaabb', f"expandir([['a', 3], ['b', 2]]) -> 'aaabb', veio {veio!r}", falhas)
    veio = expandir([])
    _verificar(veio == '', f"expandir([]) -> '', veio {veio!r}", falhas)
    veio = expandir([['z', 1]])
    _verificar(veio == 'z', f"expandir([['z', 1]]) -> 'z', veio {veio!r}", falhas)
    try:
        expandir([['a', 0]])
        _verificar(False, "expandir([['a', 0]]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "expandir([['a', 0]]) levanta ValueError", falhas)
    try:
        expandir([['ab', 1]])
        _verificar(False, "expandir([['ab', 1]]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "expandir([['ab', 1]]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

