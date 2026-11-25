"""
Exercicio 10 — Fila de um caixa

Um caixa so atende uma pessoa por vez.
Cada cliente e {"chegada": int, "duracao": int}, ja na ordem de chegada.
duracao e o tempo de atendimento, em minutos.

Implemente esperas(clientes) -> list[int].

Para cada cliente, a espera e quantos minutos ele fica parado antes de ser atendido.
- se o caixa estiver livre na chegada, a espera e 0
- se o caixa ainda estiver ocupado, a espera e o tempo que falta
- o proximo so comeca quando o anterior termina

Regras de entrada:
- duracao: int >= 1 (bool nao vale)
- chegada: int >= 0 (bool nao vale)
- chegada menor que a do cliente anterior levanta ValueError
- lista vazia devolve []

Como testar:
    python3 logica/10_fila_caixa.py
"""


def esperas(clientes: list[dict]) -> list[int]:
    # seu codigo aqui
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(esperas([]) == [], "sem clientes", falhas)
    _verificar(
        esperas(
            [
                {"chegada": 0, "duracao": 5},
                {"chegada": 1, "duracao": 2},
                {"chegada": 10, "duracao": 1},
            ]
        )
        == [0, 4, 0],
        "espera no meio e caixa livre no fim",
        falhas,
    )
    _verificar(
        esperas(
            [
                {"chegada": 0, "duracao": 3},
                {"chegada": 3, "duracao": 1},
            ]
        )
        == [0, 0],
        "chegou exatamente quando o caixa liberou",
        falhas,
    )

    try:
        esperas([{"chegada": 0, "duracao": 0}])
        _verificar(False, "duracao 0 deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "duracao 0 levanta ValueError", falhas)

    try:
        esperas([{"chegada": 0, "duracao": True}])
        _verificar(False, "bool nao e duracao", falhas)
    except ValueError:
        _verificar(True, "duracao bool levanta ValueError", falhas)

    try:
        esperas(
            [
                {"chegada": 5, "duracao": 1},
                {"chegada": 4, "duracao": 1},
            ]
        )
        _verificar(False, "fora de ordem deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "chegada fora de ordem levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
