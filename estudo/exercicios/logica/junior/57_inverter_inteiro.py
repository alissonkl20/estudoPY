"""
Logica junior 57 — Inverter inteiro

Inverta os digitos e preserve o sinal. 100 vira 1. 0 continua 0.

Como testar:
    python3 logica/junior/57_inverter_inteiro.py
"""

def inverter_inteiro(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = inverter_inteiro(123)
    _verificar(veio == 321, f"inverter_inteiro(123) -> 321, veio {veio!r}", falhas)
    veio = inverter_inteiro(100)
    _verificar(veio == 1, f"inverter_inteiro(100) -> 1, veio {veio!r}", falhas)
    veio = inverter_inteiro(-120)
    _verificar(veio == -21, f"inverter_inteiro(-120) -> -21, veio {veio!r}", falhas)
    veio = inverter_inteiro(0)
    _verificar(veio == 0, f"inverter_inteiro(0) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

