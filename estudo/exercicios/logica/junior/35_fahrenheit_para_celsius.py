"""
Logica junior 35 — Fahrenheit para Celsius

A formula e (f - 32) * 5 / 9. Arredonde com 2 casas.

Como testar:
    python3 logica/junior/35_fahrenheit_para_celsius.py
"""

def fahrenheit_para_celsius(fahrenheit: float) -> float:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = fahrenheit_para_celsius(32)
    _verificar(veio == 0.0, f"fahrenheit_para_celsius(32) -> 0.0, veio {veio!r}", falhas)
    veio = fahrenheit_para_celsius(212)
    _verificar(veio == 100.0, f"fahrenheit_para_celsius(212) -> 100.0, veio {veio!r}", falhas)
    veio = fahrenheit_para_celsius(-40)
    _verificar(veio == -40.0, f"fahrenheit_para_celsius(-40) -> -40.0, veio {veio!r}", falhas)
    veio = fahrenheit_para_celsius(33.8)
    _verificar(veio == 1.0, f"fahrenheit_para_celsius(33.8) -> 1.0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

