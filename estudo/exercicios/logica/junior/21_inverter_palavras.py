"""
Logica junior 21 — Inverter palavras

Inverta a ordem das palavras. Espacos repetidos viram um separador e somem das pontas.

Como testar:
    python3 logica/junior/21_inverter_palavras.py
"""

def inverter_palavras(texto: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = inverter_palavras('um dois tres')
    _verificar(veio == 'tres dois um', f"inverter_palavras('um dois tres') -> 'tres dois um', veio {veio!r}", falhas)
    veio = inverter_palavras('  um   dois ')
    _verificar(veio == 'dois um', f"inverter_palavras('  um   dois ') -> 'dois um', veio {veio!r}", falhas)
    veio = inverter_palavras('')
    _verificar(veio == '', f"inverter_palavras('') -> '', veio {veio!r}", falhas)
    veio = inverter_palavras('so')
    _verificar(veio == 'so', f"inverter_palavras('so') -> 'so', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

