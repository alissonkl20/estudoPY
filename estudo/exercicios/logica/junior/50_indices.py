"""
Logica junior 50 — Indices de um valor

Devolva todos os indices em que alvo aparece, do menor para o maior. Se nao aparecer, [].

Como testar:
    python3 logica/junior/50_indices.py
"""

def indices(nums: list, alvo) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = indices([1, 2, 1], 1)
    _verificar(veio == [0, 2], f"indices([1, 2, 1], 1) -> [0, 2], veio {veio!r}", falhas)
    veio = indices([5, 5, 5], 5)
    _verificar(veio == [0, 1, 2], f"indices([5, 5, 5], 5) -> [0, 1, 2], veio {veio!r}", falhas)
    veio = indices([1, 2], 9)
    _verificar(veio == [], f"indices([1, 2], 9) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

