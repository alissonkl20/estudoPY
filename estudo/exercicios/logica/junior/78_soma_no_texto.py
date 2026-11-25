"""
Logica junior 78 — Somar numeros do texto

Some os inteiros escondidos no texto. Se nao houver numero, vale 0.

Como testar:
    python3 logica/junior/78_soma_no_texto.py
"""

def soma_no_texto(texto: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = soma_no_texto('a12b3')
    _verificar(veio == 15, f"soma_no_texto('a12b3') -> 15, veio {veio!r}", falhas)
    veio = soma_no_texto('x')
    _verificar(veio == 0, f"soma_no_texto('x') -> 0, veio {veio!r}", falhas)
    veio = soma_no_texto('')
    _verificar(veio == 0, f"soma_no_texto('') -> 0, veio {veio!r}", falhas)
    veio = soma_no_texto('007')
    _verificar(veio == 7, f"soma_no_texto('007') -> 7, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

