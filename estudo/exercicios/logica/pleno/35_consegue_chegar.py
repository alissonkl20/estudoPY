"""
Logica pleno 35 — Consegue chegar

nums[i] e o alcance maximo a partir de i. Verdadeiro se der para chegar na ultima casa. Lista vazia e verdadeira.

Como testar:
    python3 logica/pleno/35_consegue_chegar.py
"""

def consegue_chegar(nums: list[int]) -> bool:
    return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = consegue_chegar([2, 3, 1, 1, 4])
    _verificar(veio == True, f"consegue_chegar([2, 3, 1, 1, 4]) -> True, veio {veio!r}", falhas)
    veio = consegue_chegar([3, 2, 1, 0, 4])
    _verificar(veio == False, f"consegue_chegar([3, 2, 1, 0, 4]) -> False, veio {veio!r}", falhas)
    veio = consegue_chegar([0])
    _verificar(veio == True, f"consegue_chegar([0]) -> True, veio {veio!r}", falhas)
    veio = consegue_chegar([])
    _verificar(veio == True, f"consegue_chegar([]) -> True, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

