"""
Teste tecnico 07 — Troco em moedas

Nivel junior. Pague o valor com a menor quantidade de moedas.
Use sempre a maior moeda que ainda cabe.

Implemente troco(centavos) -> dict.

Moedas, nesta ordem: 100, 50, 25, 10, 5 e 1.
O dict sempre tem as seis chaves, mesmo quando a quantidade e 0.

- centavos: int maior ou igual a 0 (bool nao vale)
- 130 vira uma de 100, uma de 25 e uma de 5
- entrada invalida levanta ValueError

Como testar:
    python3 junior/07_troco.py
"""


def troco(centavos: int) -> dict:
    return {}


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def _soma(moedas: dict) -> int:
    return sum(valor * qtd for valor, qtd in moedas.items())


def testar() -> None:
    falhas: list[str] = []
    vazio = {100: 0, 50: 0, 25: 0, 10: 0, 5: 0, 1: 0}
    _verificar(troco(0) == vazio, "zero centavos", falhas)

    de_130 = troco(130)
    _verificar(
        de_130 == {100: 1, 50: 0, 25: 1, 10: 0, 5: 1, 1: 0},
        f"130, veio {de_130}",
        falhas,
    )
    if de_130:
        _verificar(_soma(de_130) == 130, "as moedas de 130 fecham o valor", falhas)

    de_99 = troco(99)
    _verificar(
        de_99 == {100: 0, 50: 1, 25: 1, 10: 2, 5: 0, 1: 4},
        f"99, veio {de_99}",
        falhas,
    )
    _verificar(troco(3) == {100: 0, 50: 0, 25: 0, 10: 0, 5: 0, 1: 3}, "so moedas de 1", falhas)

    for ruim in (-1, True, 1.5):
        try:
            troco(ruim)  # type: ignore[arg-type]
            _verificar(False, f"troco({ruim!r}) deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"troco({ruim!r}) levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
