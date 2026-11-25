"""
Logica junior 07 — Palindromo

Ignore maiusculas, espacos e o que nao for letra ou numero. Vazio, depois de limpar, e palindromo.

Como testar:
    python3 logica/junior/07_palindromo.py
"""

def palindromo(texto: str) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = palindromo('ana')
    _verificar(veio == True, f"palindromo('ana') -> True, veio {veio!r}", falhas)
    veio = palindromo('Ana')
    _verificar(veio == True, f"palindromo('Ana') -> True, veio {veio!r}", falhas)
    veio = palindromo('A base')
    _verificar(veio == False, f"palindromo('A base') -> False, veio {veio!r}", falhas)
    veio = palindromo('A man a plan a canal Panama')
    _verificar(veio == True, f"palindromo('A man a plan a canal Panama') -> True, veio {veio!r}", falhas)
    veio = palindromo('ab')
    _verificar(veio == False, f"palindromo('ab') -> False, veio {veio!r}", falhas)
    veio = palindromo('')
    _verificar(veio == True, f"palindromo('') -> True, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

