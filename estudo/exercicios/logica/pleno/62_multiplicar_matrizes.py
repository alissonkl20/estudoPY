"""
Logica pleno 62 — Multiplicar matrizes

A quantidade de colunas da primeira precisa ser a de linhas da segunda. Senao, ou se alguma for vazia, levante ValueError.

Como testar:
    python3 logica/pleno/62_multiplicar_matrizes.py
"""

def multiplicar_matrizes(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = multiplicar_matrizes([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    _verificar(veio == [[19, 22], [43, 50]], f"multiplicar_matrizes([[1, 2], [3, 4]], [[5, 6], [7, 8]]) -> [[19, 22], [43, 50]], veio {veio!r}", falhas)
    try:
        multiplicar_matrizes([[1, 2]], [[1]])
        _verificar(False, "multiplicar_matrizes([[1, 2]], [[1]]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "multiplicar_matrizes([[1, 2]], [[1]]) levanta ValueError", falhas)
    try:
        multiplicar_matrizes([], [[1]])
        _verificar(False, "multiplicar_matrizes([], [[1]]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "multiplicar_matrizes([], [[1]]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

