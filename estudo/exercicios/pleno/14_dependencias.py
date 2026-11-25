"""
Teste tecnico 14 — Ordem das dependencias

Nivel pleno. Cada tarefa so pode rodar depois dos pre-requisitos.
Se varias estiverem livres ao mesmo tempo, escolha so uma: a que vem
primeiro no alfabeto. Depois disso, veja de novo quem ficou livre.

Implemente ordenar(tarefas) -> list[str].

tarefas mapeia o nome para a lista de pre-requisitos.
- pre-requisito que nao existe como tarefa levanta ValueError
- ciclo levanta ValueError
- dicionario vazio devolve []

Como testar:
    python3 pleno/14_dependencias.py
"""


def ordenar(tarefas: dict[str, list[str]]) -> list[str]:
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(ordenar({}) == [], "sem tarefas", falhas)
    _verificar(
        ordenar({"b": ["a"], "c": [], "a": []}) == ["a", "b", "c"],
        "escolhe uma livre, a primeira do alfabeto",
        falhas,
    )
    _verificar(
        ordenar(
            {
                "relatorio": ["extrair", "limpar"],
                "extrair": [],
                "limpar": ["extrair"],
            }
        )
        == ["extrair", "limpar", "relatorio"],
        "pre-requisito vem antes",
        falhas,
    )

    _verificar(
        ordenar({"b": ["z"], "z": []}) == ["z", "b"],
        "dependencia simples",
        falhas,
    )

    try:
        ordenar({"b": ["fantasma"]})
        _verificar(False, "dependencia ausente deveria falhar", falhas)
    except ValueError:
        _verificar(True, "dependencia ausente levanta ValueError", falhas)

    try:
        ordenar({"a": ["b"], "b": ["a"]})
        _verificar(False, "ciclo deveria falhar", falhas)
    except ValueError:
        _verificar(True, "ciclo levanta ValueError", falhas)

    try:
        ordenar({"a": ["a"]})
        _verificar(False, "auto dependencia deveria falhar", falhas)
    except ValueError:
        _verificar(True, "auto dependencia levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
