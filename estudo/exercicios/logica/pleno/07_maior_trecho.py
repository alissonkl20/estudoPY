"""
Logica pleno 07 — Trecho sem repetir

Devolva o tamanho do maior trecho sem caractere repetido. Vazio vale 0.

Como testar:
    python3 logica/pleno/07_maior_trecho.py
"""

def maior_trecho(texto: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = maior_trecho('abcabcbb')
    _verificar(veio == 3, f"maior_trecho('abcabcbb') -> 3, veio {veio!r}", falhas)
    veio = maior_trecho('bbbbb')
    _verificar(veio == 1, f"maior_trecho('bbbbb') -> 1, veio {veio!r}", falhas)
    veio = maior_trecho('pwwkew')
    _verificar(veio == 3, f"maior_trecho('pwwkew') -> 3, veio {veio!r}", falhas)
    veio = maior_trecho('')
    _verificar(veio == 0, f"maior_trecho('') -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

