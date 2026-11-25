"""Solucao de pleno/07_cache_lru.py. Tente resolver o enunciado antes de abrir."""


class CacheLRU:
    def __init__(self, capacidade: int):
        if isinstance(capacidade, bool) or not isinstance(capacidade, int) or capacidade < 1:
            raise ValueError("capacidade invalida")
        self.capacidade = capacidade
        self._dados: dict = {}

    def get(self, chave):
        if chave not in self._dados:
            return None
        valor = self._dados.pop(chave)
        self._dados[chave] = valor
        return valor

    def put(self, chave, valor) -> None:
        if chave in self._dados:
            self._dados.pop(chave)
        elif len(self._dados) >= self.capacidade:
            mais_antigo = next(iter(self._dados))
            del self._dados[mais_antigo]
        self._dados[chave] = valor

    def __len__(self) -> int:
        return len(self._dados)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(CacheLRU=CacheLRU)
