"""Solucao de junior/08_agenda.py. Tente resolver o enunciado antes de abrir."""


class Agenda:
    def __init__(self) -> None:
        self._contatos: dict[str, str] = {}

    def adicionar(self, nome: str, telefone: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("nome invalido")
        if not isinstance(telefone, str):
            raise ValueError("telefone invalido")
        telefone = telefone.strip()
        if not telefone.isdigit() or len(telefone) not in (10, 11):
            raise ValueError("telefone invalido")
        nome = nome.strip()
        if nome in self._contatos:
            raise ValueError("contato repetido")
        self._contatos[nome] = telefone

    def buscar(self, nome: str) -> str | None:
        if not isinstance(nome, str):
            return None
        return self._contatos.get(nome.strip())

    def remover(self, nome: str) -> bool:
        if not isinstance(nome, str):
            return False
        nome = nome.strip()
        if nome not in self._contatos:
            return False
        del self._contatos[nome]
        return True

    def listar(self) -> list[str]:
        return sorted(self._contatos)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Agenda=Agenda)
