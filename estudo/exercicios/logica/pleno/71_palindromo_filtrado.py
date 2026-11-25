"""
Logica pleno 71 — Palindromo filtrado

Ignore o que nao e letra nem numero, e ignore maiusculas.

Como testar:
    python3 logica/pleno/71_palindromo_filtrado.py
"""

def palindromo_filtrado(texto: str) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = palindromo_filtrado('A man, a plan, a canal: Panama')
    _verificar(veio == True, f"palindromo_filtrado('A man, a plan, a canal: Panama') -> True, veio {veio!r}", falhas)
    veio = palindromo_filtrado('race a car')
    _verificar(veio == False, f"palindromo_filtrado('race a car') -> False, veio {veio!r}", falhas)
    veio = palindromo_filtrado('')
    _verificar(veio == True, f"palindromo_filtrado('') -> True, veio {veio!r}", falhas)
    veio = palindromo_filtrado('0P')
    _verificar(veio == False, f"palindromo_filtrado('0P') -> False, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

