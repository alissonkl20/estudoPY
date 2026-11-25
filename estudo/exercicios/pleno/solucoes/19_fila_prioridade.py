"""Solucao de pleno/19_fila_prioridade.py. Tente resolver o enunciado antes de abrir."""

import heapq


class FilaPrioridade:
    def __init__(self) -> None:
        self._itens: list[tuple[int, int, object]] = []
        self._ordem = 0

    def adicionar(self, item, prioridade: int) -> None:
        if isinstance(prioridade, bool) or not isinstance(prioridade, int):
            raise ValueError("prioridade invalida")
        heapq.heappush(self._itens, (prioridade, self._ordem, item))
        self._ordem += 1

    def proximo(self):
        if not self._itens:
            raise ValueError("fila vazia")
        return heapq.heappop(self._itens)[2]

    def __len__(self) -> int:
        return len(self._itens)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(FilaPrioridade=FilaPrioridade)
