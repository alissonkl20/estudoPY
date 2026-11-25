"""
Logica pleno 18 — Girar matriz

Gire uma matriz quadrada 90 graus no sentido horario. Devolva outra matriz. Matriz que nao e quadrada levanta ValueError.

Como testar:
    python3 logica/pleno/18_girar_horario.py
"""

def girar_horario(matriz: list[list[int]]) -> list[list[int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = girar_horario([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    _verificar(veio == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], f"girar_horario([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[7, 4, 1], [8, 5, 2], [9, 6, 3]], veio {veio!r}", falhas)
    veio = girar_horario([[1]])
    _verificar(veio == [[1]], f"girar_horario([[1]]) -> [[1]], veio {veio!r}", falhas)
    try:
        girar_horario([[1, 2]])
        _verificar(False, "girar_horario([[1, 2]]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "girar_horario([[1, 2]]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

