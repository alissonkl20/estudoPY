"""
Logica junior 55 — Esta no intervalo

Verdadeiro se n estiver entre inicio e fim, inclusive.

Como testar:
    python3 logica/junior/55_entre.py
"""

def entre(n: int, inicio: int, fim: int) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = entre(3, 1, 5)
    _verificar(veio == True, f"entre(3, 1, 5) -> True, veio {veio!r}", falhas)
    veio = entre(1, 1, 5)
    _verificar(veio == True, f"entre(1, 1, 5) -> True, veio {veio!r}", falhas)
    veio = entre(0, 1, 5)
    _verificar(veio == False, f"entre(0, 1, 5) -> False, veio {veio!r}", falhas)
    veio = entre(5, 1, 5)
    _verificar(veio == True, f"entre(5, 1, 5) -> True, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

