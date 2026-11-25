"""
Logica pleno 17 — Ordem espiral

Percorra a matriz em espiral, no sentido horario, de fora para dentro. Matriz vazia devolve [].

Como testar:
    python3 logica/pleno/17_espiral.py
"""

def espiral(matriz: list[list[int]]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = espiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    _verificar(veio == [1, 2, 3, 6, 9, 8, 7, 4, 5], f"espiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 2, 3, 6, 9, 8, 7, 4, 5], veio {veio!r}", falhas)
    veio = espiral([[1, 2], [3, 4]])
    _verificar(veio == [1, 2, 4, 3], f"espiral([[1, 2], [3, 4]]) -> [1, 2, 4, 3], veio {veio!r}", falhas)
    veio = espiral([])
    _verificar(veio == [], f"espiral([]) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

