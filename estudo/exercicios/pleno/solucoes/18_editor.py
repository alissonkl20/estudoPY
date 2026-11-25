"""Solucao de pleno/18_editor.py. Tente resolver o enunciado antes de abrir."""


class Editor:
    def __init__(self) -> None:
        self.texto = ""
        self._historico = [""]
        self._indice = 0

    def _gravar(self, novo: str) -> None:
        self._historico = self._historico[: self._indice + 1]
        self._historico.append(novo)
        self._indice += 1
        self.texto = novo

    def inserir(self, trecho: str) -> None:
        if not isinstance(trecho, str) or trecho == "":
            raise ValueError("trecho invalido")
        self._gravar(self.texto + trecho)

    def apagar(self, n: int) -> None:
        if isinstance(n, bool) or not isinstance(n, int) or n < 1 or n > len(self.texto):
            raise ValueError("quantidade invalida")
        self._gravar(self.texto[:-n])

    def desfazer(self) -> None:
        if self._indice == 0:
            raise ValueError("nada para desfazer")
        self._indice -= 1
        self.texto = self._historico[self._indice]

    def refazer(self) -> None:
        if self._indice + 1 >= len(self._historico):
            raise ValueError("nada para refazer")
        self._indice += 1
        self.texto = self._historico[self._indice]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Editor=Editor)
