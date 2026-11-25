"""
Logica junior 54 — Mediana de tres

Devolva o valor do meio entre tres inteiros.

Como testar:
    python3 logica/junior/54_mediana_tres.py
"""

def mediana_tres(a: int, b: int, c: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = mediana_tres(3, 1, 2)
    _verificar(veio == 2, f"mediana_tres(3, 1, 2) -> 2, veio {veio!r}", falhas)
    veio = mediana_tres(5, 5, 1)
    _verificar(veio == 5, f"mediana_tres(5, 5, 1) -> 5, veio {veio!r}", falhas)
    veio = mediana_tres(-1, -3, -2)
    _verificar(veio == -2, f"mediana_tres(-1, -3, -2) -> -2, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

