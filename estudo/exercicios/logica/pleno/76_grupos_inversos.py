"""
Logica pleno 76 — Inverter em grupos

Inverta cada grupo de k itens. O ultimo grupo, se for menor que k, fica como esta. k menor que 1 levanta ValueError. Devolva outra lista.

Como testar:
    python3 logica/pleno/76_grupos_inversos.py
"""

def grupos_inversos(nums: list[int], k: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = grupos_inversos([1, 2, 3, 4, 5], 2)
    _verificar(veio == [2, 1, 4, 3, 5], f"grupos_inversos([1, 2, 3, 4, 5], 2) -> [2, 1, 4, 3, 5], veio {veio!r}", falhas)
    veio = grupos_inversos([1, 2, 3, 4, 5], 3)
    _verificar(veio == [3, 2, 1, 4, 5], f"grupos_inversos([1, 2, 3, 4, 5], 3) -> [3, 2, 1, 4, 5], veio {veio!r}", falhas)
    veio = grupos_inversos([1, 2], 3)
    _verificar(veio == [1, 2], f"grupos_inversos([1, 2], 3) -> [1, 2], veio {veio!r}", falhas)
    try:
        grupos_inversos([1], 0)
        _verificar(False, "grupos_inversos([1], 0) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "grupos_inversos([1], 0) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

