"""
Logica pleno 10 — Distancia de edicao

Conte o minimo de insercoes, remocoes e trocas para transformar a em b.

Como testar:
    python3 logica/pleno/10_distancia_edicao.py
"""

def distancia_edicao(a: str, b: str) -> int:
    return 0


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    veio = distancia_edicao('kitten', 'sitting')
    _verificar(veio == 3, f"distancia_edicao('kitten', 'sitting') -> 3, veio {veio!r}", falhas)
    veio = distancia_edicao('', 'a')
    _verificar(veio == 1, f"distancia_edicao('', 'a') -> 1, veio {veio!r}", falhas)
    veio = distancia_edicao('a', 'a')
    _verificar(veio == 0, f"distancia_edicao('a', 'a') -> 0, veio {veio!r}", falhas)
    veio = distancia_edicao('ab', 'ba')
    _verificar(veio == 2, f"distancia_edicao('ab', 'ba') -> 2, veio {veio!r}", falhas)
    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()

