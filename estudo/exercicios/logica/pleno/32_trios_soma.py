"""
Logica pleno 32 — Trios que somam zero

Devolva os trios unicos que somam zero. Cada trio vem ordenado, e a lista tambem.

Como testar:
    python3 logica/pleno/32_trios_soma.py
"""

def trios_soma(nums: list[int]) -> list[list[int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = trios_soma([-1, 0, 1, 2, -1, -4])
    _verificar(veio == [[-1, -1, 2], [-1, 0, 1]], f"trios_soma([-1, 0, 1, 2, -1, -4]) -> [[-1, -1, 2], [-1, 0, 1]], veio {veio!r}", falhas)
    veio = trios_soma([0, 0, 0])
    _verificar(veio == [[0, 0, 0]], f"trios_soma([0, 0, 0]) -> [[0, 0, 0]], veio {veio!r}", falhas)
    veio = trios_soma([])
    _verificar(veio == [], f"trios_soma([]) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

