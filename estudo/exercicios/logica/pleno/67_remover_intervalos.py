"""
Logica pleno 67 — Remover intervalos

Intervalos [inicio, fim), fim exclusivo. Devolva quantos remover para nenhum cruzar. Encostar pode ficar. Lista vazia vale 0.

Como testar:
    python3 logica/pleno/67_remover_intervalos.py
"""

def remover_intervalos(intervalos: list[tuple[int, int]]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = remover_intervalos([(1, 2), (2, 3), (1, 3)])
    _verificar(veio == 1, f"remover_intervalos([(1, 2), (2, 3), (1, 3)]) -> 1, veio {veio!r}", falhas)
    veio = remover_intervalos([(1, 2), (1, 2), (1, 2)])
    _verificar(veio == 2, f"remover_intervalos([(1, 2), (1, 2), (1, 2)]) -> 2, veio {veio!r}", falhas)
    veio = remover_intervalos([])
    _verificar(veio == 0, f"remover_intervalos([]) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

