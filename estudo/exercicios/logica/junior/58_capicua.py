"""
Logica junior 58 — Numero capicua

Verdadeiro se os digitos forem iguais nos dois sentidos. Negativo e falso.

Como testar:
    python3 logica/junior/58_capicua.py
"""

def capicua(n: int) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = capicua(121)
    _verificar(veio == True, f"capicua(121) -> True, veio {veio!r}", falhas)
    veio = capicua(10)
    _verificar(veio == False, f"capicua(10) -> False, veio {veio!r}", falhas)
    veio = capicua(0)
    _verificar(veio == True, f"capicua(0) -> True, veio {veio!r}", falhas)
    veio = capicua(-121)
    _verificar(veio == False, f"capicua(-121) -> False, veio {veio!r}", falhas)
    veio = capicua(7)
    _verificar(veio == True, f"capicua(7) -> True, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

