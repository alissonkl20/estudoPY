"""
Logica pleno 05 — Varias compras e vendas

Pode comprar e vender varias vezes, sem estoque sobreposto. Some todas as subidas.

Como testar:
    python3 logica/pleno/05_lucro_varios.py
"""

def lucro_varios(precos: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = lucro_varios([7, 1, 5, 3, 6, 4])
    _verificar(veio == 7, f"lucro_varios([7, 1, 5, 3, 6, 4]) -> 7, veio {veio!r}", falhas)
    veio = lucro_varios([1, 2, 3, 4, 5])
    _verificar(veio == 4, f"lucro_varios([1, 2, 3, 4, 5]) -> 4, veio {veio!r}", falhas)
    veio = lucro_varios([7, 6])
    _verificar(veio == 0, f"lucro_varios([7, 6]) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

