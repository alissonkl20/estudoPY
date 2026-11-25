"""
Logica junior 34 — Celsius para Fahrenheit

A formula e c * 9 / 5 + 32. Arredonde com 2 casas.

Como testar:
    python3 logica/junior/34_celsius_para_fahrenheit.py
"""

def celsius_para_fahrenheit(celsius: float) -> float:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = celsius_para_fahrenheit(0)
    _verificar(veio == 32.0, f"celsius_para_fahrenheit(0) -> 32.0, veio {veio!r}", falhas)
    veio = celsius_para_fahrenheit(100)
    _verificar(veio == 212.0, f"celsius_para_fahrenheit(100) -> 212.0, veio {veio!r}", falhas)
    veio = celsius_para_fahrenheit(1)
    _verificar(veio == 33.8, f"celsius_para_fahrenheit(1) -> 33.8, veio {veio!r}", falhas)
    veio = celsius_para_fahrenheit(-40)
    _verificar(veio == -40.0, f"celsius_para_fahrenheit(-40) -> -40.0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

