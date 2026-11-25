"""
Teste tecnico 17 — Arvore de categorias

Nivel pleno. A arvore e um dicionario com "nome" e "filhos".
Percorra em pre-ordem: o no, depois cada filho da esquerda para a direita.

Implemente caminho(arvore, nome) e descendentes(arvore, nome).

caminho devolve a lista de nomes da raiz ate o no, inclusive.
Se o nome nao existe, devolve None.

descendentes devolve os nomes abaixo do no, sem incluir o proprio.
Se o nome nao existe, devolve None. Folha devolve [].

Como testar:
    python3 pleno/17_arvore_categorias.py
"""


def caminho(arvore: dict, nome: str) -> list[str] | None:
    return None


def descendentes(arvore: dict, nome: str) -> list[str] | None:
    return None


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


ARVORE = {
    "nome": "loja",
    "filhos": [
        {"nome": "roupas", "filhos": [{"nome": "camisas", "filhos": []}]},
        {"nome": "casa", "filhos": []},
    ],
}


def testar() -> None:
    falhas: list[str] = []

    _verificar(caminho(ARVORE, "loja") == ["loja"], "caminho da raiz", falhas)
    _verificar(
        caminho(ARVORE, "camisas") == ["loja", "roupas", "camisas"],
        "caminho ate a folha",
        falhas,
    )
    _verificar(caminho(ARVORE, "nenhuma") is None, "nome ausente", falhas)
    _verificar(
        descendentes(ARVORE, "loja") == ["roupas", "camisas", "casa"],
        "pre-ordem dos descendentes",
        falhas,
    )
    _verificar(descendentes(ARVORE, "camisas") == [], "folha nao tem filhos", falhas)
    _verificar(descendentes(ARVORE, "nenhuma") is None, "descendentes ausentes", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
