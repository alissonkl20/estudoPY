"""
Logica pleno 04 — Uma compra e uma venda

Escolha um dia para comprar e outro depois para vender. Se nao houver lucro, devolva 0.

Como testar:
    python3 logica/pleno/04_lucro_unico.py
"""

def lucro_unico(precos: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = lucro_unico([7, 1, 5, 3, 6, 4])
    _verificar(veio == 5, f"lucro_unico([7, 1, 5, 3, 6, 4]) -> 5, veio {veio!r}", falhas)
    veio = lucro_unico([7, 6, 4, 3])
    _verificar(veio == 0, f"lucro_unico([7, 6, 4, 3]) -> 0, veio {veio!r}", falhas)
    veio = lucro_unico([])
    _verificar(veio == 0, f"lucro_unico([]) -> 0, veio {veio!r}", falhas)
    veio = lucro_unico([1, 2])
    _verificar(veio == 1, f"lucro_unico([1, 2]) -> 1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

