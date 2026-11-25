"""
Logica junior 26 — Potencia de dois

1 vale 2 elevado a 0 e e potencia. 0 e negativo nao sao.

Como testar:
    python3 logica/junior/26_potencia_de_dois.py
"""

def potencia_de_dois(n: int) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = potencia_de_dois(1)
    _verificar(veio == True, f"potencia_de_dois(1) -> True, veio {veio!r}", falhas)
    veio = potencia_de_dois(2)
    _verificar(veio == True, f"potencia_de_dois(2) -> True, veio {veio!r}", falhas)
    veio = potencia_de_dois(3)
    _verificar(veio == False, f"potencia_de_dois(3) -> False, veio {veio!r}", falhas)
    veio = potencia_de_dois(8)
    _verificar(veio == True, f"potencia_de_dois(8) -> True, veio {veio!r}", falhas)
    veio = potencia_de_dois(0)
    _verificar(veio == False, f"potencia_de_dois(0) -> False, veio {veio!r}", falhas)
    veio = potencia_de_dois(-2)
    _verificar(veio == False, f"potencia_de_dois(-2) -> False, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

