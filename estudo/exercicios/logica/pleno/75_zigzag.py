"""
Logica pleno 75 — Texto em zigzag

Escreva o texto em zigue-zague com a quantidade de linhas pedida e leia linha a linha. Uma linha devolve o proprio texto. linhas menor que 1 levanta ValueError.

Como testar:
    python3 logica/pleno/75_zigzag.py
"""

def zigzag(texto: str, linhas: int) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = zigzag('PAYPALISHIRING', 3)
    _verificar(veio == 'PAHNAPLSIIGYIR', f"zigzag('PAYPALISHIRING', 3) -> 'PAHNAPLSIIGYIR', veio {veio!r}", falhas)
    veio = zigzag('AB', 1)
    _verificar(veio == 'AB', f"zigzag('AB', 1) -> 'AB', veio {veio!r}", falhas)
    veio = zigzag('', 3)
    _verificar(veio == '', f"zigzag('', 3) -> '', veio {veio!r}", falhas)
    try:
        zigzag('abc', 0)
        _verificar(False, "zigzag('abc', 0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "zigzag('abc', 0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

