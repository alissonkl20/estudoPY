"""
Logica junior 15 — Dias do mes

Mes de 1 a 12. Fevereiro tem 29 no ano bissexto. Mes fora dessa faixa levanta ValueError.

Como testar:
    python3 logica/junior/15_dias_do_mes.py
"""

def dias_do_mes(mes: int, ano: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = dias_do_mes(2, 2024)
    _verificar(veio == 29, f"dias_do_mes(2, 2024) -> 29, veio {veio!r}", falhas)
    veio = dias_do_mes(2, 2023)
    _verificar(veio == 28, f"dias_do_mes(2, 2023) -> 28, veio {veio!r}", falhas)
    veio = dias_do_mes(2, 1900)
    _verificar(veio == 28, f"dias_do_mes(2, 1900) -> 28, veio {veio!r}", falhas)
    veio = dias_do_mes(2, 2000)
    _verificar(veio == 29, f"dias_do_mes(2, 2000) -> 29, veio {veio!r}", falhas)
    veio = dias_do_mes(4, 2024)
    _verificar(veio == 30, f"dias_do_mes(4, 2024) -> 30, veio {veio!r}", falhas)
    veio = dias_do_mes(1, 2024)
    _verificar(veio == 31, f"dias_do_mes(1, 2024) -> 31, veio {veio!r}", falhas)
    try:
        dias_do_mes(13, 2024)
        _verificar(False, "dias_do_mes(13, 2024) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "dias_do_mes(13, 2024) levanta ValueError", falhas)
    try:
        dias_do_mes(0, 2024)
        _verificar(False, "dias_do_mes(0, 2024) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "dias_do_mes(0, 2024) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

