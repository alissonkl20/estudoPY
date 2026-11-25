"""
Logica pleno 70 — Palindromo com uma retirada

Verdadeiro se o texto ja e palindromo ou fica palindromo apagando no maximo um caractere.

Como testar:
    python3 logica/pleno/70_palindromo_flexivel.py
"""

def palindromo_flexivel(texto: str) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = palindromo_flexivel('aba')
    _verificar(veio == True, f"palindromo_flexivel('aba') -> True, veio {veio!r}", falhas)
    veio = palindromo_flexivel('abca')
    _verificar(veio == True, f"palindromo_flexivel('abca') -> True, veio {veio!r}", falhas)
    veio = palindromo_flexivel('abc')
    _verificar(veio == False, f"palindromo_flexivel('abc') -> False, veio {veio!r}", falhas)
    veio = palindromo_flexivel('')
    _verificar(veio == True, f"palindromo_flexivel('') -> True, veio {veio!r}", falhas)
    veio = palindromo_flexivel('a')
    _verificar(veio == True, f"palindromo_flexivel('a') -> True, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

