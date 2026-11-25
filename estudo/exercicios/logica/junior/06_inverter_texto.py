"""
Logica junior 06 — Inverter texto

Devolva o texto de tras para frente. Texto vazio continua vazio.

Como testar:
    python3 logica/junior/06_inverter_texto.py
"""

def inverter_texto(texto: str) -> str:
    return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = inverter_texto('abcd')
    _verificar(veio == 'dcba', f"inverter_texto('abcd') -> 'dcba', veio {veio!r}", falhas)
    veio = inverter_texto('')
    _verificar(veio == '', f"inverter_texto('') -> '', veio {veio!r}", falhas)
    veio = inverter_texto('a')
    _verificar(veio == 'a', f"inverter_texto('a') -> 'a', veio {veio!r}", falhas)
    veio = inverter_texto('ana')
    _verificar(veio == 'ana', f"inverter_texto('ana') -> 'ana', veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

