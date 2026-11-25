"""
Logica junior 73 — Prefixo comum

Devolva o maior texto que e prefixo dos dois. Se nao houver, devolva vazio.

Como testar:
    python3 logica/junior/73_prefixo_comum.py
"""

def prefixo_comum(a: str, b: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = prefixo_comum('flor', 'fluxo')
    _verificar(veio == 'fl', f"prefixo_comum('flor', 'fluxo') -> 'fl', veio {veio!r}", falhas)
    veio = prefixo_comum('abc', 'xyz')
    _verificar(veio == '', f"prefixo_comum('abc', 'xyz') -> '', veio {veio!r}", falhas)
    veio = prefixo_comum('teste', 'teste')
    _verificar(veio == 'teste', f"prefixo_comum('teste', 'teste') -> 'teste', veio {veio!r}", falhas)
    veio = prefixo_comum('', 'a')
    _verificar(veio == '', f"prefixo_comum('', 'a') -> '', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

