"""
Logica pleno 29 — Palindromo mais longo

Devolva o tamanho do maior trecho continuo que e palindromo. Vazio vale 0.

Como testar:
    python3 logica/pleno/29_comprimento_palindromo.py
"""

def comprimento_palindromo(texto: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = comprimento_palindromo('babad')
    _verificar(veio == 3, f"comprimento_palindromo('babad') -> 3, veio {veio!r}", falhas)
    veio = comprimento_palindromo('cbbd')
    _verificar(veio == 2, f"comprimento_palindromo('cbbd') -> 2, veio {veio!r}", falhas)
    veio = comprimento_palindromo('a')
    _verificar(veio == 1, f"comprimento_palindromo('a') -> 1, veio {veio!r}", falhas)
    veio = comprimento_palindromo('')
    _verificar(veio == 0, f"comprimento_palindromo('') -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

