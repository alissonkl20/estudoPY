"""
Logica pleno 09 — Subsequencia comum

Devolva o tamanho da maior subsequencia comum. Nao precisa ser continua.

Como testar:
    python3 logica/pleno/09_lcs.py
"""

def lcs(a: str, b: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = lcs('abcde', 'ace')
    _verificar(veio == 3, f"lcs('abcde', 'ace') -> 3, veio {veio!r}", falhas)
    veio = lcs('abc', 'def')
    _verificar(veio == 0, f"lcs('abc', 'def') -> 0, veio {veio!r}", falhas)
    veio = lcs('', 'a')
    _verificar(veio == 0, f"lcs('', 'a') -> 0, veio {veio!r}", falhas)
    veio = lcs('aaa', 'aa')
    _verificar(veio == 2, f"lcs('aaa', 'aa') -> 2, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

