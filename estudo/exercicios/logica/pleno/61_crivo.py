"""
Logica pleno 61 — Crivo

Liste os primos menores ou iguais a n. n menor que 2 devolve [].

Como testar:
    python3 logica/pleno/61_crivo.py
"""

def crivo(n: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = crivo(10)
    _verificar(veio == [2, 3, 5, 7], f"crivo(10) -> [2, 3, 5, 7], veio {veio!r}", falhas)
    veio = crivo(1)
    _verificar(veio == [], f"crivo(1) -> [], veio {veio!r}", falhas)
    veio = crivo(2)
    _verificar(veio == [2], f"crivo(2) -> [2], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

