"""Solucao de pleno/20_estoque.py. Tente resolver o enunciado antes de abrir."""


class Estoque:
    def __init__(self, saldo: dict[str, int]):
        self._saldo: dict[str, int] = {}
        for sku, qtd in saldo.items():
            if isinstance(qtd, bool) or not isinstance(qtd, int) or qtd < 0:
                raise ValueError("saldo invalido")
            self._saldo[sku] = qtd
        self._reservas: dict[str, tuple[str, int]] = {}
        self._seq = 0

    def disponivel(self, sku: str) -> int:
        if sku not in self._saldo:
            raise ValueError("sku desconhecido")
        return self._saldo[sku]

    def reservar(self, sku: str, qtd: int) -> str:
        if isinstance(qtd, bool) or not isinstance(qtd, int) or qtd < 1:
            raise ValueError("quantidade invalida")
        if sku not in self._saldo:
            raise ValueError("sku desconhecido")
        if qtd > self._saldo[sku]:
            raise ValueError("estoque insuficiente")
        self._saldo[sku] -= qtd
        self._seq += 1
        ident = f"r{self._seq}"
        self._reservas[ident] = (sku, qtd)
        return ident

    def confirmar(self, reserva_id: str) -> None:
        if reserva_id not in self._reservas:
            raise ValueError("reserva inexistente")
        del self._reservas[reserva_id]

    def cancelar(self, reserva_id: str) -> None:
        if reserva_id not in self._reservas:
            raise ValueError("reserva inexistente")
        sku, qtd = self._reservas.pop(reserva_id)
        self._saldo[sku] += qtd


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Estoque=Estoque)
