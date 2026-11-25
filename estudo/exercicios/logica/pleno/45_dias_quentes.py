"""
Logica pleno 45 — Dias mais quentes

Para cada dia, quantos dias ate um dia estritamente mais quente. Se nao houver, 0.

Como testar:
    python3 logica/pleno/45_dias_quentes.py
"""

def dias_quentes(temps: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = dias_quentes([73, 74, 75, 71, 69, 72, 76, 73])
    _verificar(veio == [1, 1, 4, 2, 1, 1, 0, 0], f"dias_quentes([73, 74, 75, 71, 69, 72, 76, 73]) -> [1, 1, 4, 2, 1, 1, 0, 0], veio {veio!r}", falhas)
    veio = dias_quentes([])
    _verificar(veio == [], f"dias_quentes([]) -> [], veio {veio!r}", falhas)
    veio = dias_quentes([30])
    _verificar(veio == [0], f"dias_quentes([30]) -> [0], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

