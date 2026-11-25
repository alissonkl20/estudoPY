"""
Logica pleno 15 — Perimetro da terra

1 e terra e 0 e agua. Cada lado de terra encostado em agua ou na borda conta 1.

Como testar:
    python3 logica/pleno/15_perimetro_terra.py
"""

def perimetro_terra(grade: list[list[int]]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = perimetro_terra([[1]])
    _verificar(veio == 4, f"perimetro_terra([[1]]) -> 4, veio {veio!r}", falhas)
    veio = perimetro_terra([[1, 1]])
    _verificar(veio == 6, f"perimetro_terra([[1, 1]]) -> 6, veio {veio!r}", falhas)
    veio = perimetro_terra([[1, 0], [0, 1]])
    _verificar(veio == 8, f"perimetro_terra([[1, 0], [0, 1]]) -> 8, veio {veio!r}", falhas)
    veio = perimetro_terra([])
    _verificar(veio == 0, f"perimetro_terra([]) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

