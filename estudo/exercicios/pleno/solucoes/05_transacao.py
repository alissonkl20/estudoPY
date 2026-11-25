"""Solucao de pleno/05_transacao.py. Tente resolver o enunciado antes de abrir."""

import copy
from contextlib import contextmanager


class BancoMemoria:
    def __init__(self, dados: dict | None = None):
        self.dados = copy.deepcopy(dados) if dados is not None else {}


@contextmanager
def transacao(banco: BancoMemoria):
    snapshot = copy.deepcopy(banco.dados)
    try:
        yield banco
    except Exception:
        banco.dados = snapshot
        raise


if __name__ == "__main__":
    from _rodar import rodar

    rodar(BancoMemoria=BancoMemoria, transacao=transacao)
