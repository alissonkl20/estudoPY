"""
Logica junior 13 — Contar digitos

0 tem um digito. No negativo, ignore o sinal.

Como testar:
    python3 logica/junior/13_contar_digitos.py
"""

def contar_digitos(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = contar_digitos(0)
    _verificar(veio == 1, f"contar_digitos(0) -> 1, veio {veio!r}", falhas)
    veio = contar_digitos(19)
    _verificar(veio == 2, f"contar_digitos(19) -> 2, veio {veio!r}", falhas)
    veio = contar_digitos(-100)
    _verificar(veio == 3, f"contar_digitos(-100) -> 3, veio {veio!r}", falhas)
    veio = contar_digitos(7)
    _verificar(veio == 1, f"contar_digitos(7) -> 1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

