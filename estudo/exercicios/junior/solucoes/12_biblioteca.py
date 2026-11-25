"""Solucao de junior/12_biblioteca.py. Tente resolver o enunciado antes de abrir."""


class Biblioteca:
    def __init__(self) -> None:
        self._livros: dict[str, bool] = {}

    def cadastrar(self, titulo: str) -> None:
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("titulo invalido")
        titulo = titulo.strip()
        if titulo in self._livros:
            raise ValueError("titulo repetido")
        self._livros[titulo] = True

    def emprestar(self, titulo: str) -> None:
        if titulo not in self._livros or not self._livros[titulo]:
            raise ValueError("nao pode emprestar")
        self._livros[titulo] = False

    def devolver(self, titulo: str) -> None:
        if titulo not in self._livros or self._livros[titulo]:
            raise ValueError("nao pode devolver")
        self._livros[titulo] = True

    def disponiveis(self) -> list[str]:
        return sorted(titulo for titulo, livre in self._livros.items() if livre)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Biblioteca=Biblioteca)
