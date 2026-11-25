"""
Teste tecnico 12 — Biblioteca

Nivel junior. Cadastre livros, empreste e devolva. Um livro emprestado
nao aparece na lista de disponiveis e nao pode sair de novo.

Implemente Biblioteca.

cadastrar(titulo)
- str nao vazia depois do strip; guarde sem espacos nas pontas
- titulo repetido levanta ValueError

emprestar(titulo) marca como indisponivel
- titulo desconhecido, ou ja emprestado, levanta ValueError

devolver(titulo) marca como disponivel
- titulo desconhecido, ou que ja estava na estante, levanta ValueError

disponiveis() -> lista dos titulos disponiveis, em ordem alfabetica
devolve uma lista nova

Como testar:
    python3 junior/12_biblioteca.py
"""


class Biblioteca:
    def cadastrar(self, titulo: str) -> None:
        return None

    def emprestar(self, titulo: str) -> None:
        return None

    def devolver(self, titulo: str) -> None:
        return None

    def disponiveis(self) -> list[str]:
        return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    biblioteca = Biblioteca()
    biblioteca.cadastrar("  Dom Casmurro ")
    _verificar(biblioteca.disponiveis() == ["Dom Casmurro"], "cadastra sem espaco extra", falhas)
    biblioteca.cadastrar("Capitaes")
    biblioteca.emprestar("Dom Casmurro")
    _verificar(biblioteca.disponiveis() == ["Capitaes"], "emprestado sai da lista", falhas)
    biblioteca.devolver("Dom Casmurro")
    _verificar(
        biblioteca.disponiveis() == ["Capitaes", "Dom Casmurro"],
        "devolvido volta em ordem alfabetica",
        falhas,
    )

    lista = biblioteca.disponiveis()
    if lista:
        lista.append("hack")
        _verificar("hack" not in biblioteca.disponiveis(), "disponiveis devolve copia", falhas)
    else:
        _verificar(False, "disponiveis devolve copia", falhas)

    biblioteca.emprestar("Dom Casmurro")
    try:
        biblioteca.emprestar("Dom Casmurro")
        _verificar(False, "emprestar de novo deveria falhar", falhas)
    except ValueError:
        _verificar(biblioteca.disponiveis() == ["Capitaes"], "continua emprestado", falhas)

    biblioteca.devolver("Dom Casmurro")
    try:
        biblioteca.devolver("Dom Casmurro")
        _verificar(False, "devolver quem ja esta na estante deveria falhar", falhas)
    except ValueError:
        _verificar(True, "devolver disponivel levanta ValueError", falhas)

    try:
        biblioteca.emprestar("Nenhum")
        _verificar(False, "titulo desconhecido deveria falhar", falhas)
    except ValueError:
        _verificar(True, "titulo desconhecido levanta ValueError", falhas)

    try:
        biblioteca.cadastrar("Dom Casmurro")
        _verificar(False, "titulo repetido deveria falhar", falhas)
    except ValueError:
        _verificar(True, "titulo repetido levanta ValueError", falhas)

    try:
        biblioteca.cadastrar("   ")
        _verificar(False, "titulo vazio deveria falhar", falhas)
    except ValueError:
        _verificar(True, "titulo vazio levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
