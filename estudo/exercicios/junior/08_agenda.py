"""
Teste tecnico 08 — Agenda de contatos

Nivel junior. Guarde nome e telefone. A busca e a remocao usam o nome
depois do strip. Maiuscula e minuscula continuam diferentes.

Implemente Agenda.

adicionar(nome, telefone)
- nome: str nao vazia depois do strip
- telefone: str so com digitos, 10 ou 11 caracteres, depois do strip
- nome repetido levanta ValueError e nao troca o telefone antigo
- entrada invalida levanta ValueError e nao grava

buscar(nome) -> str ou None
remover(nome) -> bool. True se removeu, False se o nome nao estava
listar() -> nomes em ordem alfabetica

Como testar:
    python3 junior/08_agenda.py
"""


class Agenda:
    def adicionar(self, nome: str, telefone: str) -> None:
        return None

    def buscar(self, nome: str) -> str | None:
        return None

    def remover(self, nome: str) -> bool:
        return False

    def listar(self) -> list[str]:
        return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    agenda = Agenda()
    agenda.adicionar(" Ana ", "11999998888")
    agenda.adicionar("Bruno", "1133334444")
    _verificar(agenda.buscar(" Ana ") == "11999998888", "busca ignora espaco da ponta", falhas)
    _verificar(agenda.buscar("ana") is None, "busca diferencia maiuscula", falhas)
    _verificar(agenda.listar() == ["Ana", "Bruno"], f"lista ordenada, veio {agenda.listar()}", falhas)

    _verificar(agenda.remover("Ana"), "remove quem existe", falhas)
    _verificar(agenda.buscar("Ana") is None and agenda.listar() == ["Bruno"], "sumiu da agenda", falhas)
    _verificar(agenda.remover("Ana") is False, "remover de novo devolve False", falhas)

    try:
        agenda.adicionar("Bruno", "11988887777")
        _verificar(False, "nome repetido deveria falhar", falhas)
    except ValueError:
        _verificar(agenda.buscar("Bruno") == "1133334444", "repetido nao troca o telefone", falhas)

    for nome, telefone in ((" ", "11999998888"), ("Caio", "123"), ("Caio", "11a9998888"), ("Caio", 11999998888)):
        try:
            Agenda().adicionar(nome, telefone)  # type: ignore[arg-type]
            _verificar(False, f"adicionar({nome!r}, {telefone!r}) deveria falhar", falhas)
        except ValueError:
            _verificar(True, f"adicionar({nome!r}, {telefone!r}) levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
