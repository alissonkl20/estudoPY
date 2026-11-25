"""
Logica junior 46 — Somar duas listas

Some item a item. Tamanhos diferentes levantam ValueError.

Como testar:
    python3 logica/junior/46_somar_listas.py
"""

def somar_listas(a: list[int], b: list[int]) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = somar_listas([1, 2], [3, 4])
    _verificar(veio == [4, 6], f"somar_listas([1, 2], [3, 4]) -> [4, 6], veio {veio!r}", falhas)
    veio = somar_listas([], [])
    _verificar(veio == [], f"somar_listas([], []) -> [], veio {veio!r}", falhas)
    veio = somar_listas([5], [-1])
    _verificar(veio == [4], f"somar_listas([5], [-1]) -> [4], veio {veio!r}", falhas)
    try:
        somar_listas([1], [1, 2])
        _verificar(False, "somar_listas([1], [1, 2]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "somar_listas([1], [1, 2]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

