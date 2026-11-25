"""
Logica pleno 74 — Compactar texto

Troque cada bloco por letra e quantidade. Se o resultado nao ficar menor que o original, devolva o original.

Como testar:
    python3 logica/pleno/74_compactar_texto.py
"""

def compactar_texto(texto: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = compactar_texto('aabcccccaaa')
    _verificar(veio == 'a2b1c5a3', f"compactar_texto('aabcccccaaa') -> 'a2b1c5a3', veio {veio!r}", falhas)
    veio = compactar_texto('abc')
    _verificar(veio == 'abc', f"compactar_texto('abc') -> 'abc', veio {veio!r}", falhas)
    veio = compactar_texto('aaa')
    _verificar(veio == 'a3', f"compactar_texto('aaa') -> 'a3', veio {veio!r}", falhas)
    veio = compactar_texto('aa')
    _verificar(veio == 'aa', f"compactar_texto('aa') -> 'aa', veio {veio!r}", falhas)
    veio = compactar_texto('')
    _verificar(veio == '', f"compactar_texto('') -> '', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

