"""
Logica pleno 33 — Ordenar zeros uns e dois

A lista so tem 0, 1 e 2. Devolva outra lista ordenada.

Como testar:
    python3 logica/pleno/33_ordenar_012.py
"""

def ordenar_012(nums: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = ordenar_012([2, 0, 2, 1, 1, 0])
    _verificar(veio == [0, 0, 1, 1, 2, 2], f"ordenar_012([2, 0, 2, 1, 1, 0]) -> [0, 0, 1, 1, 2, 2], veio {veio!r}", falhas)
    veio = ordenar_012([])
    _verificar(veio == [], f"ordenar_012([]) -> [], veio {veio!r}", falhas)
    veio = ordenar_012([2, 2])
    _verificar(veio == [2, 2], f"ordenar_012([2, 2]) -> [2, 2], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

