"""
Logica junior 62 — Numero faltante

A lista contem cada inteiro de 0 ate len(nums), inclusive, exceto um. Devolva o que falta.

Como testar:
    python3 logica/junior/62_numero_faltante.py
"""

def numero_faltante(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = numero_faltante([0, 1, 3])
    _verificar(veio == 2, f"numero_faltante([0, 1, 3]) -> 2, veio {veio!r}", falhas)
    veio = numero_faltante([1, 2, 3])
    _verificar(veio == 0, f"numero_faltante([1, 2, 3]) -> 0, veio {veio!r}", falhas)
    veio = numero_faltante([0])
    _verificar(veio == 1, f"numero_faltante([0]) -> 1, veio {veio!r}", falhas)
    veio = numero_faltante([])
    _verificar(veio == 0, f"numero_faltante([]) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

