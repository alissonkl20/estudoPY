"""
Logica pleno 58 — Busca na matriz

Cada linha esta ordenada, e o primeiro de uma linha e maior que o ultimo da anterior. Verdadeiro se o alvo existir.

Como testar:
    python3 logica/pleno/58_busca_matriz.py
"""

def busca_matriz(matriz: list[list[int]], alvo: int) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = busca_matriz([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9)
    _verificar(veio == True, f"busca_matriz([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9) -> True, veio {veio!r}", falhas)
    veio = busca_matriz([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 2)
    _verificar(veio == False, f"busca_matriz([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 2) -> False, veio {veio!r}", falhas)
    veio = busca_matriz([], 1)
    _verificar(veio == False, f"busca_matriz([], 1) -> False, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

