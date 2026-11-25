"""
Exercicio 05 — Fechar um pedido

Antes de cobrar, o backend calcula subtotal, desconto, frete e total.
Esta funcao e a regra de negocio, separada do banco e do HTTP.

Implemente calcular_pedido(itens, cupom=None) -> dict.

Cada item e {"nome": str, "preco": numero, "qtd": int}.

Regras:
- carrinho vazio: subtotal 0, desconto 0, frete 0, total 0
- preco precisa ser int ou float, maior ou igual a 0 (bool nao vale)
- qtd precisa ser int maior ou igual a 1 (bool nao vale)
- entrada invalida levanta ValueError
- subtotal = soma de preco * qtd
- cupom "DESC10" tira 10% do subtotal; qualquer outro cupom tira 0
- frete e 0 quando o subtotal (antes do desconto) e pelo menos 100; senao, 15
- total = subtotal - desconto + frete
- subtotal, desconto, frete e total com 2 casas decimais (round)

Como testar:
    python3 exercicios/05_calcular_pedido.py
"""


def calcular_pedido(itens: list[dict], cupom: str | None = None) -> dict:
    # seu codigo aqui
    return {}


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    vazio = calcular_pedido([])
    _verificar(
        vazio == {"subtotal": 0.0, "desconto": 0.0, "frete": 0.0, "total": 0.0},
        f"carrinho vazio, veio {vazio}",
        falhas,
    )

    com_frete = calcular_pedido(
        [{"nome": "Caderno", "preco": 40, "qtd": 2}],
    )
    _verificar(
        com_frete
        == {"subtotal": 80.0, "desconto": 0.0, "frete": 15.0, "total": 95.0},
        f"frete cobrado, veio {com_frete}",
        falhas,
    )

    gratis = calcular_pedido(
        [{"nome": "Tenis", "preco": 60, "qtd": 2}],
        cupom="DESC10",
    )
    _verificar(
        gratis
        == {"subtotal": 120.0, "desconto": 12.0, "frete": 0.0, "total": 108.0},
        f"frete gratis com cupom, veio {gratis}",
        falhas,
    )

    cupom_ruim = calcular_pedido(
        [{"nome": "Caneta", "preco": 10, "qtd": 1}],
        cupom="NATAL",
    )
    _verificar(cupom_ruim["desconto"] == 0.0, "cupom desconhecido nao da desconto", falhas)
    _verificar(cupom_ruim["total"] == 25.0, "total com frete e sem desconto", falhas)

    limite = calcular_pedido([{"nome": "Livro", "preco": 100, "qtd": 1}])
    _verificar(limite["frete"] == 0.0 and limite["total"] == 100.0, "subtotal 100 tem frete 0", falhas)

    try:
        calcular_pedido([{"nome": "X", "preco": -1, "qtd": 1}])
        _verificar(False, "preco negativo deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "preco negativo levanta ValueError", falhas)

    try:
        calcular_pedido([{"nome": "X", "preco": True, "qtd": 1}])
        _verificar(False, "preco bool deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "preco bool levanta ValueError", falhas)

    try:
        calcular_pedido([{"nome": "X", "preco": 10, "qtd": 0}])
        _verificar(False, "qtd 0 deveria levantar ValueError", falhas)
    except ValueError:
        _verificar(True, "qtd 0 levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
