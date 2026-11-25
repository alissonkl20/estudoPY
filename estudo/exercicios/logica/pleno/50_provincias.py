"""
Logica pleno 50 — Provincias

n cidades numeradas de 0 a n-1. Cada par e uma estrada nos dois sentidos. Conte os grupos ligados. n menor que 1 levanta ValueError.

Como testar:
    python3 logica/pleno/50_provincias.py
"""

def provincias(n: int, estradas: list[list[int]]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = provincias(4, [[0, 1], [1, 2]])
    _verificar(veio == 2, f"provincias(4, [[0, 1], [1, 2]]) -> 2, veio {veio!r}", falhas)
    veio = provincias(1, [])
    _verificar(veio == 1, f"provincias(1, []) -> 1, veio {veio!r}", falhas)
    veio = provincias(3, [[0, 1], [1, 2], [2, 0]])
    _verificar(veio == 1, f"provincias(3, [[0, 1], [1, 2], [2, 0]]) -> 1, veio {veio!r}", falhas)
    try:
        provincias(0, [])
        _verificar(False, "provincias(0, []) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "provincias(0, []) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

