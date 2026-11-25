"""
Logica pleno 14 — Caminho de menor soma

Grade de inteiros. Ande so para a direita ou para baixo. Devolva a menor soma. Grade vazia levanta ValueError.

Como testar:
    python3 logica/pleno/14_soma_caminho.py
"""

def soma_caminho(grade: list[list[int]]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = soma_caminho([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    _verificar(veio == 7, f"soma_caminho([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) -> 7, veio {veio!r}", falhas)
    veio = soma_caminho([[1]])
    _verificar(veio == 1, f"soma_caminho([[1]]) -> 1, veio {veio!r}", falhas)
    try:
        soma_caminho([])
        _verificar(False, "soma_caminho([]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "soma_caminho([]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

