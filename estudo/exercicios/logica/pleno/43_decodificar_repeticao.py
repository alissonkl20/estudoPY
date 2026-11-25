"""
Logica pleno 43 — Decodificar repeticao

3[a] vira aaa. Pode aninhar: 3[a2[c]] vira accaccacc. Colchete sem fechar levanta ValueError. Vazio devolve vazio.

Como testar:
    python3 logica/pleno/43_decodificar_repeticao.py
"""

def decodificar_repeticao(texto: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = decodificar_repeticao('3[a]2[bc]')
    _verificar(veio == 'aaabcbc', f"decodificar_repeticao('3[a]2[bc]') -> 'aaabcbc', veio {veio!r}", falhas)
    veio = decodificar_repeticao('3[a2[c]]')
    _verificar(veio == 'accaccacc', f"decodificar_repeticao('3[a2[c]]') -> 'accaccacc', veio {veio!r}", falhas)
    veio = decodificar_repeticao('2[ab]')
    _verificar(veio == 'abab', f"decodificar_repeticao('2[ab]') -> 'abab', veio {veio!r}", falhas)
    veio = decodificar_repeticao('')
    _verificar(veio == '', f"decodificar_repeticao('') -> '', veio {veio!r}", falhas)
    try:
        decodificar_repeticao('3[')
        _verificar(False, "decodificar_repeticao('3[') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "decodificar_repeticao('3[') levanta ValueError", falhas)
    try:
        decodificar_repeticao(']')
        _verificar(False, "decodificar_repeticao(']') deveria falhar", falhas)
    except ValueError:
        _verificar(True, "decodificar_repeticao(']') levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

