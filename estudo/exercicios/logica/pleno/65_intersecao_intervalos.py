"""
Logica pleno 65 — Intersecao de intervalos

Intervalos inclusivos (inicio, fim). Devolva a intersecao, ou None se nao houver. inicio maior que fim levanta ValueError. Encostar conta.

Como testar:
    python3 logica/pleno/65_intersecao_intervalos.py
"""

def intersecao_intervalos(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int] | None:
    return None


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = intersecao_intervalos((1, 5), (3, 7))
    _verificar(veio == (3, 5), f"intersecao_intervalos((1, 5), (3, 7)) -> (3, 5), veio {veio!r}", falhas)
    veio = intersecao_intervalos((1, 2), (3, 4))
    _verificar(veio == None, f"intersecao_intervalos((1, 2), (3, 4)) -> None, veio {veio!r}", falhas)
    veio = intersecao_intervalos((1, 3), (3, 5))
    _verificar(veio == (3, 3), f"intersecao_intervalos((1, 3), (3, 5)) -> (3, 3), veio {veio!r}", falhas)
    try:
        intersecao_intervalos((3, 1), (0, 2))
        _verificar(False, "intersecao_intervalos((3, 1), (0, 2)) deveria falhar", falhas)
    except ValueError:
        _verificar(True, "intersecao_intervalos((3, 1), (0, 2)) levanta ValueError", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

