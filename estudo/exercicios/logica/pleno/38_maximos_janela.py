"""
Logica pleno 38 — Maximos da janela

Para cada janela de tamanho k, devolva o maior. k menor que 1 ou maior que a lista levanta ValueError.

Como testar:
    python3 logica/pleno/38_maximos_janela.py
"""

def maximos_janela(nums: list[int], k: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = maximos_janela([1, 3, -1, -3, 5, 3, 6, 7], 3)
    _verificar(veio == [3, 3, 5, 5, 6, 7], f"maximos_janela([1, 3, -1, -3, 5, 3, 6, 7], 3) -> [3, 3, 5, 5, 6, 7], veio {veio!r}", falhas)
    veio = maximos_janela([1], 1)
    _verificar(veio == [1], f"maximos_janela([1], 1) -> [1], veio {veio!r}", falhas)
    try:
        maximos_janela([1, 2], 0)
        _verificar(False, "maximos_janela([1, 2], 0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "maximos_janela([1, 2], 0) levanta ValueError", falhas)
    try:
        maximos_janela([1], 2)
        _verificar(False, "maximos_janela([1], 2) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "maximos_janela([1], 2) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

