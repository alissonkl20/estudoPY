"""
Logica pleno 46 — Proximo maior a direita

Para cada posicao, o primeiro valor estritamente maior a direita. Se nao houver, -1.

Como testar:
    python3 logica/pleno/46_proximo_maior.py
"""

def proximo_maior(nums: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = proximo_maior([2, 1, 2, 4, 3])
    _verificar(veio == [4, 2, 4, -1, -1], f"proximo_maior([2, 1, 2, 4, 3]) -> [4, 2, 4, -1, -1], veio {veio!r}", falhas)
    veio = proximo_maior([1, 2])
    _verificar(veio == [2, -1], f"proximo_maior([1, 2]) -> [2, -1], veio {veio!r}", falhas)
    veio = proximo_maior([])
    _verificar(veio == [], f"proximo_maior([]) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

