"""
Logica pleno 49 — Retangulo no histograma

Cada barra tem largura 1. Devolva a maior area retangular. Lista vazia vale 0.

Como testar:
    python3 logica/pleno/49_retangulo_histograma.py
"""

def retangulo_histograma(alturas: list[int]) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = retangulo_histograma([2, 1, 5, 6, 2, 3])
    _verificar(veio == 10, f"retangulo_histograma([2, 1, 5, 6, 2, 3]) -> 10, veio {veio!r}", falhas)
    veio = retangulo_histograma([2, 2, 2])
    _verificar(veio == 6, f"retangulo_histograma([2, 2, 2]) -> 6, veio {veio!r}", falhas)
    veio = retangulo_histograma([])
    _verificar(veio == 0, f"retangulo_histograma([]) -> 0, veio {veio!r}", falhas)
    veio = retangulo_histograma([0])
    _verificar(veio == 0, f"retangulo_histograma([0]) -> 0, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

