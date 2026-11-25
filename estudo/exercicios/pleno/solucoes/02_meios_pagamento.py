"""Solucao de pleno/02_meios_pagamento.py. Tente resolver o enunciado antes de abrir."""

from abc import ABC, abstractmethod


def _valor(valor: float) -> float:
    if isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor <= 0:
        raise ValueError("valor invalido")
    return round(float(valor), 2)


class MeioPagamento(ABC):
    nome = ""

    @abstractmethod
    def calcular_taxa(self, valor: float) -> float:
        raise NotImplementedError

    def processar(self, valor: float) -> dict:
        quantia = _valor(valor)
        taxa = round(float(self.calcular_taxa(quantia)), 2)
        return {
            "meio": self.nome,
            "valor": quantia,
            "taxa": taxa,
            "liquido": round(quantia - taxa, 2),
        }


class CartaoCredito(MeioPagamento):
    nome = "cartao"

    def calcular_taxa(self, valor: float) -> float:
        return round(valor * 0.03, 2)


class Pix(MeioPagamento):
    nome = "pix"

    def calcular_taxa(self, valor: float) -> float:
        return 0.0


class Boleto(MeioPagamento):
    nome = "boleto"

    def calcular_taxa(self, valor: float) -> float:
        if valor <= 2.5:
            raise ValueError("valor insuficiente para boleto")
        return 2.5


def criar_meio(nome: str) -> MeioPagamento:
    meios = {
        "cartao": CartaoCredito,
        "pix": Pix,
        "boleto": Boleto,
    }
    if nome not in meios:
        raise ValueError("meio desconhecido")
    return meios[nome]()


if __name__ == "__main__":
    from _rodar import rodar

    rodar(
        MeioPagamento=MeioPagamento,
        CartaoCredito=CartaoCredito,
        Pix=Pix,
        Boleto=Boleto,
        criar_meio=criar_meio,
    )
