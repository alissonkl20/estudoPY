"""
Logica junior 11 — Primos ate n

Liste os primos de 2 ate n, inclusive, em ordem. Se n for menor que 2, devolva [].

Como testar:
    python3 logica/junior/11_primos_ate.py
"""

def primos_ate(n: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = primos_ate(10)
    _verificar(veio == [2, 3, 5, 7], f"primos_ate(10) -> [2, 3, 5, 7], veio {veio!r}", falhas)
    veio = primos_ate(2)
    _verificar(veio == [2], f"primos_ate(2) -> [2], veio {veio!r}", falhas)
    veio = primos_ate(1)
    _verificar(veio == [], f"primos_ate(1) -> [], veio {veio!r}", falhas)
    veio = primos_ate(20)
    _verificar(veio == [2, 3, 5, 7, 11, 13, 17, 19], f"primos_ate(20) -> [2, 3, 5, 7, 11, 13, 17, 19], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

