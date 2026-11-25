"""
Teste tecnico 09 — Juntar itens da compra

Nivel junior. Some a quantidade dos itens com o mesmo nome.
O nome entra na ordem em que apareceu pela primeira vez.

Implemente consolidar(itens) -> list[dict].

Cada item e {"nome": str, "qtd": int}.
- nome vazio depois do strip levanta ValueError
- qtd: int maior ou igual a 1 (bool nao vale)
- grave o nome sem espacos nas pontas
- nao altere a lista recebida
- lista vazia devolve []

Como testar:
    python3 junior/09_compras.py
"""


def consolidar(itens: list[dict]) -> list[dict]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    itens = [
        {"nome": " Arroz ", "qtd": 2},
        {"nome": "Feijao", "qtd": 1},
        {"nome": "Arroz", "qtd": 3},
    ]
    copia = [dict(item) for item in itens]
    _verificar(
        consolidar(itens) == [{"nome": "Arroz", "qtd": 5}, {"nome": "Feijao", "qtd": 1}],
        "soma quem repete",
        falhas,
    )
    _verificar(itens == copia, "lista original intacta", falhas)
    _verificar(consolidar([]) == [], "lista vazia", falhas)

    for ruim in (
        [{"nome": " ", "qtd": 1}],
        [{"nome": "Arroz", "qtd": 0}],
        [{"nome": "Arroz", "qtd": True}],
    ):
        try:
            consolidar(ruim)
            _verificar(False, f"{ruim!r} deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"{ruim!r} levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
