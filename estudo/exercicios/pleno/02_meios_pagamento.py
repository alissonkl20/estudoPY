"""
Teste tecnico 02 — Meios de pagamento

Nivel pleno. Uma classe base define o contrato. Cada meio calcula a propria taxa.
Quem chama processar nao precisa saber qual classe concreta esta usando.

Implemente MeioPagamento, CartaoCredito, Pix, Boleto e criar_meio(nome).

processar(valor) devolve:
    {"meio": str, "valor": float, "taxa": float, "liquido": float}

Regras comuns:
- valor: int ou float > 0 (bool nao vale); senao ValueError
- valor, taxa e liquido com 2 casas (round)
- liquido = valor - taxa

Taxas:
- cartao: 3% do valor
- pix: 0
- boleto: 2.50 fixos; se o valor for menor ou igual a 2.50, ValueError

criar_meio aceita "cartao", "pix" e "boleto". Outro nome levanta ValueError.
Cada chamada devolve uma instancia nova.

Como testar:
    python3 pleno/02_meios_pagamento.py
"""

from abc import ABC, abstractmethod


class MeioPagamento(ABC):
    nome = ""

    @abstractmethod
    def calcular_taxa(self, valor: float) -> float:
        # seu codigo aqui
        return 0.0

    def processar(self, valor: float) -> dict:
        # seu codigo aqui
        return {}


class CartaoCredito(MeioPagamento):
    nome = "cartao"

    def calcular_taxa(self, valor: float) -> float:
        # seu codigo aqui
        return 0.0


class Pix(MeioPagamento):
    nome = "pix"

    def calcular_taxa(self, valor: float) -> float:
        # seu codigo aqui
        return 0.0


class Boleto(MeioPagamento):
    nome = "boleto"

    def calcular_taxa(self, valor: float) -> float:
        # seu codigo aqui
        return 0.0


def criar_meio(nome: str) -> MeioPagamento:
    # seu codigo aqui
    return CartaoCredito()


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    cartao = criar_meio("cartao").processar(100)
    _verificar(
        cartao == {"meio": "cartao", "valor": 100.0, "taxa": 3.0, "liquido": 97.0},
        f"cartao, veio {cartao}",
        falhas,
    )
    pix = criar_meio("pix").processar(10)
    _verificar(
        pix == {"meio": "pix", "valor": 10.0, "taxa": 0.0, "liquido": 10.0},
        f"pix, veio {pix}",
        falhas,
    )
    boleto = criar_meio("boleto").processar(10)
    _verificar(
        boleto == {"meio": "boleto", "valor": 10.0, "taxa": 2.5, "liquido": 7.5},
        f"boleto, veio {boleto}",
        falhas,
    )
    _verificar(criar_meio("cartao") is not criar_meio("cartao"), "instancia nova", falhas)

    for nome in ("cartao", "pix", "boleto"):
        try:
            criar_meio(nome).processar(True)  # type: ignore[arg-type]
            _verificar(False, f"{nome} aceitou bool", falhas)
        except ValueError:
            _verificar(True, f"{nome} rejeita bool", falhas)

    try:
        criar_meio("boleto").processar(2.5)
        _verificar(False, "boleto barato deveria falhar", falhas)
    except ValueError:
        _verificar(True, "boleto de 2.50 levanta ValueError", falhas)

    try:
        criar_meio("dinheiro")
        _verificar(False, "meio desconhecido deveria falhar", falhas)
    except ValueError:
        _verificar(True, "meio desconhecido levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
