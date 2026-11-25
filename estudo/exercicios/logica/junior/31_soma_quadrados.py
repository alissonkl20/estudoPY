"""
Logica junior 31 — Soma dos quadrados

Some 1**2 + 2**2 + ... + n**2. n igual a 0 vale 0. n negativo levanta ValueError.

Como testar:
    python3 logica/junior/31_soma_quadrados.py
"""

def soma_quadrados(n: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = soma_quadrados(0)
    _verificar(veio == 0, f"soma_quadrados(0) -> 0, veio {veio!r}", falhas)
    veio = soma_quadrados(3)
    _verificar(veio == 14, f"soma_quadrados(3) -> 14, veio {veio!r}", falhas)
    veio = soma_quadrados(1)
    _verificar(veio == 1, f"soma_quadrados(1) -> 1, veio {veio!r}", falhas)
    veio = soma_quadrados(10)
    _verificar(veio == 385, f"soma_quadrados(10) -> 385, veio {veio!r}", falhas)
    try:
        soma_quadrados(-1)
        _verificar(False, "soma_quadrados(-1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "soma_quadrados(-1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

