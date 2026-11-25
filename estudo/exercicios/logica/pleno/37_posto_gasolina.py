"""
Logica pleno 37 — Posto de gasolina

gas[i] e o que abastece, cost[i] e o que gasta ate o proximo. Devolva o indice de onde da para completar a volta. Se nao der, -1. Listas de tamanhos diferentes ou vazias devolvem -1.

Como testar:
    python3 logica/pleno/37_posto_gasolina.py
"""

def posto_gasolina(gas: list[int], custo: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = posto_gasolina([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    _verificar(veio == 3, f"posto_gasolina([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) -> 3, veio {veio!r}", falhas)
    veio = posto_gasolina([2, 3, 4], [3, 4, 3])
    _verificar(veio == -1, f"posto_gasolina([2, 3, 4], [3, 4, 3]) -> -1, veio {veio!r}", falhas)
    veio = posto_gasolina([], [])
    _verificar(veio == -1, f"posto_gasolina([], []) -> -1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

