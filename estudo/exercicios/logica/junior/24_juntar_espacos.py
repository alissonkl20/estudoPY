"""
Logica junior 24 — Juntar espacos

Tire espacos das pontas e troque sequencias de espaco por um so.

Como testar:
    python3 logica/junior/24_juntar_espacos.py
"""

def juntar_espacos(texto: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = juntar_espacos('  a   b  ')
    _verificar(veio == 'a b', f"juntar_espacos('  a   b  ') -> 'a b', veio {veio!r}", falhas)
    veio = juntar_espacos('')
    _verificar(veio == '', f"juntar_espacos('') -> '', veio {veio!r}", falhas)
    veio = juntar_espacos('   ')
    _verificar(veio == '', f"juntar_espacos('   ') -> '', veio {veio!r}", falhas)
    veio = juntar_espacos('a')
    _verificar(veio == 'a', f"juntar_espacos('a') -> 'a', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

