"""
Logica pleno 40 — Maior produto continuo

Devolva o maior produto de um trecho continuo e nao vazio. Lista vazia levanta ValueError.

Como testar:
    python3 logica/pleno/40_produto_subarray.py
"""

def produto_subarray(nums: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = produto_subarray([2, 3, -2, 4])
    _verificar(veio == 6, f"produto_subarray([2, 3, -2, 4]) -> 6, veio {veio!r}", falhas)
    veio = produto_subarray([-2, 0, -1])
    _verificar(veio == 0, f"produto_subarray([-2, 0, -1]) -> 0, veio {veio!r}", falhas)
    veio = produto_subarray([-2])
    _verificar(veio == -2, f"produto_subarray([-2]) -> -2, veio {veio!r}", falhas)
    try:
        produto_subarray([])
        _verificar(False, "produto_subarray([]) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "produto_subarray([]) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

