"""
Logica junior 42 — Rotacionar para a direita

Ande k posicoes para a direita. k maior que o tamanho da volta na lista. k negativo levanta ValueError.

Como testar:
    python3 logica/junior/42_rotacionar_direita.py
"""

def rotacionar_direita(nums: list[int], k: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = rotacionar_direita([1, 2, 3, 4], 1)
    _verificar(veio == [4, 1, 2, 3], f"rotacionar_direita([1, 2, 3, 4], 1) -> [4, 1, 2, 3], veio {veio!r}", falhas)
    veio = rotacionar_direita([1, 2, 3, 4], 5)
    _verificar(veio == [4, 1, 2, 3], f"rotacionar_direita([1, 2, 3, 4], 5) -> [4, 1, 2, 3], veio {veio!r}", falhas)
    veio = rotacionar_direita([1, 2, 3], 0)
    _verificar(veio == [1, 2, 3], f"rotacionar_direita([1, 2, 3], 0) -> [1, 2, 3], veio {veio!r}", falhas)
    try:
        rotacionar_direita([1], -1)
        _verificar(False, "rotacionar_direita([1], -1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "rotacionar_direita([1], -1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

