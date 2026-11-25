"""Solucao de pleno/10_pedido_estados.py. Tente resolver o enunciado antes de abrir."""


class TransicaoInvalida(Exception):
    pass


class Pedido:
    _transicoes = {
        "rascunho": {"confirmar": "confirmado", "cancelar": "cancelado"},
        "confirmado": {"pagar": "pago", "cancelar": "cancelado"},
        "pago": {"enviar": "enviado"},
        "enviado": {},
        "cancelado": {},
    }

    def __init__(self) -> None:
        self.estado = "rascunho"
        self.historico = ["rascunho"]

    def _ir(self, acao: str) -> None:
        destino = self._transicoes[self.estado].get(acao)
        if destino is None:
            raise TransicaoInvalida(f"nao pode {acao} a partir de {self.estado}")
        self.estado = destino
        self.historico.append(destino)

    def confirmar(self) -> None:
        self._ir("confirmar")

    def pagar(self) -> None:
        self._ir("pagar")

    def enviar(self) -> None:
        self._ir("enviar")

    def cancelar(self) -> None:
        self._ir("cancelar")


if __name__ == "__main__":
    from _rodar import rodar

    rodar(TransicaoInvalida=TransicaoInvalida, Pedido=Pedido)
