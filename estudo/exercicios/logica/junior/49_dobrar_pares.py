"""
Logica junior 49 — Dobrar os pares

Par vira o dobro. Impar permanece. Devolva uma lista nova.

Como testar:
    python3 logica/junior/49_dobrar_pares.py
"""

def dobrar_pares(nums: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = dobrar_pares([1, 2, 3, 4])
    _verificar(veio == [1, 4, 3, 8], f"dobrar_pares([1, 2, 3, 4]) -> [1, 4, 3, 8], veio {veio!r}", falhas)
    veio = dobrar_pares([-4, -3])
    _verificar(veio == [-8, -3], f"dobrar_pares([-4, -3]) -> [-8, -3], veio {veio!r}", falhas)
    veio = dobrar_pares([])
    _verificar(veio == [], f"dobrar_pares([]) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

