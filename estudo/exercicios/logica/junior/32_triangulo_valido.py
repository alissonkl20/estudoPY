"""
Logica junior 32 — Triangulo valido

Tres lados positivos formam triangulo quando a soma de dois e maior que o terceiro.

Como testar:
    python3 logica/junior/32_triangulo_valido.py
"""

def triangulo_valido(a: int, b: int, c: int) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = triangulo_valido(3, 4, 5)
    _verificar(veio == True, f"triangulo_valido(3, 4, 5) -> True, veio {veio!r}", falhas)
    veio = triangulo_valido(2, 2, 3)
    _verificar(veio == True, f"triangulo_valido(2, 2, 3) -> True, veio {veio!r}", falhas)
    veio = triangulo_valido(1, 1, 2)
    _verificar(veio == False, f"triangulo_valido(1, 1, 2) -> False, veio {veio!r}", falhas)
    veio = triangulo_valido(0, 1, 1)
    _verificar(veio == False, f"triangulo_valido(0, 1, 1) -> False, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

