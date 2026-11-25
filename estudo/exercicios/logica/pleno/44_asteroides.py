"""
Logica pleno 44 — Colisao de asteroides

Positivo anda para a direita, negativo para a esquerda. No choque, o menor explode. Empate explode os dois. Devolva o que sobra, na ordem.

Como testar:
    python3 logica/pleno/44_asteroides.py
"""

def asteroides(nums: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = asteroides([5, 10, -5])
    _verificar(veio == [5, 10], f"asteroides([5, 10, -5]) -> [5, 10], veio {veio!r}", falhas)
    veio = asteroides([8, -8])
    _verificar(veio == [], f"asteroides([8, -8]) -> [], veio {veio!r}", falhas)
    veio = asteroides([10, 2, -5])
    _verificar(veio == [10], f"asteroides([10, 2, -5]) -> [10], veio {veio!r}", falhas)
    veio = asteroides([-2, -1, 1, 2])
    _verificar(veio == [-2, -1, 1, 2], f"asteroides([-2, -1, 1, 2]) -> [-2, -1, 1, 2], veio {veio!r}", falhas)
    veio = asteroides([])
    _verificar(veio == [], f"asteroides([]) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

