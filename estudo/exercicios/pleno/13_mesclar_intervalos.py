"""
Teste tecnico 13 — Mesclar intervalos

Nivel pleno. Intervalos vem fora de ordem. Junte os que se sobrepoem
ou se encostam. Devolva uma lista nova, ordenada pelo inicio.

Implemente mesclar(intervalos) -> list[tuple[int, int]].

- cada item e (inicio, fim), inclusive
- (1, 3) e (3, 5) viram (1, 5) porque se encostam
- (1, 2) e (4, 5) continuam separados
- inicio > fim levanta ValueError e a lista original nao muda
- bool nao vale como numero
- lista vazia devolve []

Como testar:
    python3 pleno/13_mesclar_intervalos.py
"""


def mesclar(intervalos: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    dados = [(5, 5), (1, 3), (8, 10), (2, 6), (9, 12)]
    copia = list(dados)
    resultado = mesclar(dados)
    _verificar(
        resultado == [(1, 6), (8, 12)],
        f"sobreposicao e ponto interno, veio {resultado}",
        falhas,
    )
    _verificar(dados == copia, "lista original intacta", falhas)
    _verificar(mesclar([]) == [], "lista vazia", falhas)
    _verificar(mesclar([(1, 3), (3, 5)]) == [(1, 5)], "encostar tambem junta", falhas)
    _verificar(mesclar([(1, 2), (4, 5)]) == [(1, 2), (4, 5)], "intervalo no meio fica", falhas)
    _verificar(mesclar([(4, 5), (1, 2)]) == [(1, 2), (4, 5)], "entrada fora de ordem", falhas)

    try:
        mesclar([(3, 1)])
        _verificar(False, "inicio maior que fim deveria falhar", falhas)
    except ValueError:
        _verificar(True, "inicio maior que fim levanta ValueError", falhas)

    try:
        mesclar([(True, 2)])  # type: ignore[list-item]
        _verificar(False, "bool nao e limite", falhas)
    except ValueError:
        _verificar(True, "bool levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
