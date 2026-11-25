"""
Teste tecnico 24 — Papeis e permissoes

Nivel pleno. Um papel herda as permissoes dos pais. O usuario pode ter
varios papeis. Ciclo na heranca e erro de configuracao.

Implemente Acesso(papeis, heranca).

papeis: nome -> lista de permissoes proprias
heranca: nome -> lista de pais
- pai ou papel da heranca que nao existe em papeis levanta ValueError
- ciclo levanta ValueError na construcao
- pode(papeis_usuario, permissao) -> bool
- papel do usuario que nao existe levanta ValueError
- lista vazia de papeis devolve False

Como testar:
    python3 pleno/24_permissoes.py
"""


class Acesso:
    def __init__(self, papeis: dict[str, list[str]], heranca: dict[str, list[str]]):
        self.papeis = papeis
        self.heranca = heranca

    def pode(self, papeis_usuario: list[str], permissao: str) -> bool:
        return False


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    acesso = Acesso(
        {
            "viewer": ["ler"],
            "editor": ["escrever"],
            "admin": ["apagar"],
        },
        {
            "editor": ["viewer"],
            "admin": ["editor"],
        },
    )
    _verificar(acesso.pode(["editor"], "ler"), "editor herda ler", falhas)
    _verificar(acesso.pode(["editor"], "escrever"), "permissao propria", falhas)
    _verificar(not acesso.pode(["editor"], "apagar"), "editor nao apaga", falhas)
    _verificar(acesso.pode(["admin"], "ler"), "heranca em cadeia", falhas)
    _verificar(acesso.pode(["viewer", "editor"], "escrever"), "vale um dos papeis", falhas)
    _verificar(not acesso.pode([], "ler"), "sem papel nao pode", falhas)

    try:
        acesso.pode(["visitante"], "ler")
        _verificar(False, "papel desconhecido deveria falhar", falhas)
    except ValueError:
        _verificar(True, "papel desconhecido levanta ValueError", falhas)

    try:
        Acesso({"a": ["x"], "b": ["y"]}, {"a": ["b"], "b": ["a"]})
        _verificar(False, "ciclo deveria falhar", falhas)
    except ValueError:
        _verificar(True, "ciclo levanta ValueError", falhas)

    try:
        Acesso({"a": ["x"]}, {"a": ["fantasma"]})
        _verificar(False, "pai ausente deveria falhar", falhas)
    except ValueError:
        _verificar(True, "pai ausente levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
