"""
Logica junior 69 — Maiores que o limite

Devolva os numeros estritamente maiores que o limite, na ordem original.

Como testar:
    python3 logica/junior/69_maiores_que.py
"""

def maiores_que(nums: list[int], limite: int) -> list[int]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = maiores_que([1, 5, 3], 3)
    _verificar(veio == [5], f"maiores_que([1, 5, 3], 3) -> [5], veio {veio!r}", falhas)
    veio = maiores_que([3, 3], 3)
    _verificar(veio == [], f"maiores_que([3, 3], 3) -> [], veio {veio!r}", falhas)
    veio = maiores_que([], 0)
    _verificar(veio == [], f"maiores_que([], 0) -> [], veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

