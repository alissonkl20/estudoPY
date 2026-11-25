"""
Logica pleno 31 — Maior area de agua

Duas barras formam um recipiente. A area e a menor altura vezes a distancia. Menos de duas barras vale 0.

Como testar:
    python3 logica/pleno/31_maior_area.py
"""

def maior_area(alturas: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = maior_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    _verificar(veio == 49, f"maior_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) -> 49, veio {veio!r}", falhas)
    veio = maior_area([1, 1])
    _verificar(veio == 1, f"maior_area([1, 1]) -> 1, veio {veio!r}", falhas)
    veio = maior_area([1])
    _verificar(veio == 0, f"maior_area([1]) -> 0, veio {veio!r}", falhas)
    veio = maior_area([])
    _verificar(veio == 0, f"maior_area([]) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

