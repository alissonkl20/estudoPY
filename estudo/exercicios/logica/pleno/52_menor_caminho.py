"""
Logica pleno 52 — Menor caminho

O grafo mapeia um no para vizinhos (destino, peso). Pesos sao positivos. Devolva a distancia. Se nao houver caminho, -1. Origem igual ao destino vale 0.

Como testar:
    python3 logica/pleno/52_menor_caminho.py
"""

def menor_caminho(grafo: dict, origem: str, destino: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = menor_caminho({'a': [('b', 1), ('c', 4)], 'b': [('c', 1)], 'c': []}, 'a', 'c')
    _verificar(veio == 2, f"menor_caminho({{'a': [('b', 1), ('c', 4)], 'b': [('c', 1)], 'c': []}}, 'a', 'c') -> 2, veio {veio!r}", falhas)
    veio = menor_caminho({'a': []}, 'a', 'a')
    _verificar(veio == 0, f"menor_caminho({{'a': []}}, 'a', 'a') -> 0, veio {veio!r}", falhas)
    veio = menor_caminho({'a': [('b', 1)], 'b': []}, 'a', 'z')
    _verificar(veio == -1, f"menor_caminho({{'a': [('b', 1)], 'b': []}}, 'a', 'z') -> -1, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

