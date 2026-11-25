"""
Logica pleno 68 — Inserir intervalo

Os intervalos inclusivos ja vem ordenados e sem cruzar. Insira novo e junte o que encostar ou cruzar.

Como testar:
    python3 logica/pleno/68_inserir_intervalo.py
"""

def inserir_intervalo(intervalos: list[tuple[int, int]], novo: tuple[int, int]) -> list[tuple[int, int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = inserir_intervalo([(1, 3), (6, 9)], (2, 5))
    _verificar(veio == [(1, 5), (6, 9)], f"inserir_intervalo([(1, 3), (6, 9)], (2, 5)) -> [(1, 5), (6, 9)], veio {veio!r}", falhas)
    veio = inserir_intervalo([(1, 5)], (6, 8))
    _verificar(veio == [(1, 5), (6, 8)], f"inserir_intervalo([(1, 5)], (6, 8)) -> [(1, 5), (6, 8)], veio {veio!r}", falhas)
    veio = inserir_intervalo([], (1, 2))
    _verificar(veio == [(1, 2)], f"inserir_intervalo([], (1, 2)) -> [(1, 2)], veio {veio!r}", falhas)
    try:
        inserir_intervalo([], (3, 1))
        _verificar(False, "inserir_intervalo([], (3, 1)) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "inserir_intervalo([], (3, 1)) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

