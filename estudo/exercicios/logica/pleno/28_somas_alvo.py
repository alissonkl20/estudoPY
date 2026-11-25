"""
Logica pleno 28 — Somas que dao o alvo

Cada numero entra no maximo uma vez. Devolva as combinacoes ordenadas, e a lista tambem ordenada. Numeros positivos.

Como testar:
    python3 logica/pleno/28_somas_alvo.py
"""

def somas_alvo(nums: list[int], alvo: int) -> list[list[int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = somas_alvo([1, 2, 3, 6], 6)
    _verificar(veio == [[1, 2, 3], [6]], f"somas_alvo([1, 2, 3, 6], 6) -> [[1, 2, 3], [6]], veio {veio!r}", falhas)
    veio = somas_alvo([2, 3, 5], 8)
    _verificar(veio == [[3, 5]], f"somas_alvo([2, 3, 5], 8) -> [[3, 5]], veio {veio!r}", falhas)
    veio = somas_alvo([1, 2], 10)
    _verificar(veio == [], f"somas_alvo([1, 2], 10) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

