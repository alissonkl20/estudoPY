"""
Logica junior 41 — Rotacionar para a esquerda

Ande k posicoes para a esquerda. k maior que o tamanho da volta na lista. k negativo levanta ValueError. Devolva uma lista nova.

Como testar:
    python3 logica/junior/41_rotacionar_esquerda.py
"""

def rotacionar_esquerda(nums: list[int], k: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = rotacionar_esquerda([1, 2, 3, 4], 1)
    _verificar(veio == [2, 3, 4, 1], f"rotacionar_esquerda([1, 2, 3, 4], 1) -> [2, 3, 4, 1], veio {veio!r}", falhas)
    veio = rotacionar_esquerda([1, 2, 3, 4], 5)
    _verificar(veio == [2, 3, 4, 1], f"rotacionar_esquerda([1, 2, 3, 4], 5) -> [2, 3, 4, 1], veio {veio!r}", falhas)
    veio = rotacionar_esquerda([1, 2, 3], 0)
    _verificar(veio == [1, 2, 3], f"rotacionar_esquerda([1, 2, 3], 0) -> [1, 2, 3], veio {veio!r}", falhas)
    veio = rotacionar_esquerda([], 3)
    _verificar(veio == [], f"rotacionar_esquerda([], 3) -> [], veio {veio!r}", falhas)
    try:
        rotacionar_esquerda([1, 2], -1)
        _verificar(False, "rotacionar_esquerda([1, 2], -1) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "rotacionar_esquerda([1, 2], -1) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

