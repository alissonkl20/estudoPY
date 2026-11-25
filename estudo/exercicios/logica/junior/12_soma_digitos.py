"""
Logica junior 12 — Somar digitos

Some os digitos. No negativo, ignore o sinal: -19 vale 1+9.

Como testar:
    python3 logica/junior/12_soma_digitos.py
"""

def soma_digitos(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = soma_digitos(19)
    _verificar(veio == 10, f"soma_digitos(19) -> 10, veio {veio!r}", falhas)
    veio = soma_digitos(0)
    _verificar(veio == 0, f"soma_digitos(0) -> 0, veio {veio!r}", falhas)
    veio = soma_digitos(-19)
    _verificar(veio == 10, f"soma_digitos(-19) -> 10, veio {veio!r}", falhas)
    veio = soma_digitos(100)
    _verificar(veio == 1, f"soma_digitos(100) -> 1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

