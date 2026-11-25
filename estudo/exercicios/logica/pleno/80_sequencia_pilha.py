"""
Logica pleno 80 — Sequencia de pilha

pushed entra na ordem dada. popped e uma saida possivel se der para produzir com uma pilha. Tamanhos diferentes levantam ValueError.

Como testar:
    python3 logica/pleno/80_sequencia_pilha.py
"""

def sequencia_pilha(pushed: list[int], popped: list[int]) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = sequencia_pilha([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    _verificar(veio == True, f"sequencia_pilha([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) -> True, veio {veio!r}", falhas)
    veio = sequencia_pilha([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
    _verificar(veio == False, f"sequencia_pilha([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) -> False, veio {veio!r}", falhas)
    veio = sequencia_pilha([], [])
    _verificar(veio == True, f"sequencia_pilha([], []) -> True, veio {veio!r}", falhas)
    veio = sequencia_pilha([1, 2], [2, 1])
    _verificar(veio == True, f"sequencia_pilha([1, 2], [2, 1]) -> True, veio {veio!r}", falhas)
    try:
        sequencia_pilha([1], [1, 2])
        _verificar(False, "sequencia_pilha([1], [1, 2]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "sequencia_pilha([1], [1, 2]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

