"""
Logica pleno 57 — Primeira e ultima

A lista esta ordenada. Devolva (primeira, ultima) posicao do alvo. Se nao existir, (-1, -1).

Como testar:
    python3 logica/pleno/57_ocorrencias.py
"""

def ocorrencias(nums: list[int], alvo: int) -> tuple[int, int]:
    return ()


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = ocorrencias([5, 7, 7, 8, 8, 10], 8)
    _verificar(veio == (3, 4), f"ocorrencias([5, 7, 7, 8, 8, 10], 8) -> (3, 4), veio {veio!r}", falhas)
    veio = ocorrencias([5, 7, 7, 8, 8, 10], 6)
    _verificar(veio == (-1, -1), f"ocorrencias([5, 7, 7, 8, 8, 10], 6) -> (-1, -1), veio {veio!r}", falhas)
    veio = ocorrencias([], 1)
    _verificar(veio == (-1, -1), f"ocorrencias([], 1) -> (-1, -1), veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

