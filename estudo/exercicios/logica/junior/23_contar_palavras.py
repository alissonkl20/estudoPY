"""
Logica junior 23 — Contar palavras

Palavra e um bloco separado por espaco. Texto vazio tem 0.

Como testar:
    python3 logica/junior/23_contar_palavras.py
"""

def contar_palavras(texto: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = contar_palavras('um dois')
    _verificar(veio == 2, f"contar_palavras('um dois') -> 2, veio {veio!r}", falhas)
    veio = contar_palavras('  a   b  ')
    _verificar(veio == 2, f"contar_palavras('  a   b  ') -> 2, veio {veio!r}", falhas)
    veio = contar_palavras('')
    _verificar(veio == 0, f"contar_palavras('') -> 0, veio {veio!r}", falhas)
    veio = contar_palavras('so')
    _verificar(veio == 1, f"contar_palavras('so') -> 1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

