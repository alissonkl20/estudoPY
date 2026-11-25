"""
Logica pleno 06 — Subarrays com soma

Conte os trechos continuos cuja soma e k. Negativos entram.

Como testar:
    python3 logica/pleno/06_contar_subarrays.py
"""

def contar_subarrays(nums: list[int], k: int) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = contar_subarrays([1, 1, 1], 2)
    _verificar(veio == 2, f"contar_subarrays([1, 1, 1], 2) -> 2, veio {veio!r}", falhas)
    veio = contar_subarrays([1, -1, 0], 0)
    _verificar(veio == 3, f"contar_subarrays([1, -1, 0], 0) -> 3, veio {veio!r}", falhas)
    veio = contar_subarrays([1], 0)
    _verificar(veio == 0, f"contar_subarrays([1], 0) -> 0, veio {veio!r}", falhas)
    veio = contar_subarrays([], 0)
    _verificar(veio == 0, f"contar_subarrays([], 0) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

