"""Solucao de pleno/15_limite_requisicoes.py. Tente resolver o enunciado antes de abrir."""


class LimiteRequisicoes:
    def __init__(self, maximo: int, janela: int):
        if isinstance(maximo, bool) or not isinstance(maximo, int) or maximo < 1:
            raise ValueError("maximo invalido")
        if isinstance(janela, bool) or not isinstance(janela, int) or janela < 1:
            raise ValueError("janela invalida")
        self.maximo = maximo
        self.janela = janela
        self._hits: list[int] = []

    def permitir(self, agora: int) -> bool:
        if isinstance(agora, bool) or not isinstance(agora, int):
            raise ValueError("instante invalido")
        self._hits = [instante for instante in self._hits if agora - instante < self.janela]
        if len(self._hits) >= self.maximo:
            return False
        self._hits.append(agora)
        return True


if __name__ == "__main__":
    from _rodar import rodar

    rodar(LimiteRequisicoes=LimiteRequisicoes)
