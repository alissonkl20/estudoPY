"""Solucao do exercicio 05. Tente resolver o arquivo em exercicios/ antes de abrir."""


def calcular_pedido(itens: list[dict], cupom: str | None = None) -> dict:
    if not itens:
        return {"subtotal": 0.0, "desconto": 0.0, "frete": 0.0, "total": 0.0}

    for item in itens:
        preco = item["preco"]
        qtd = item["qtd"]
        if type(preco) not in (int, float) or preco < 0:
            raise ValueError("preco invalido")
        if type(qtd) is not int or qtd < 1:
            raise ValueError("qtd invalida")

    subtotal = round(sum(item["preco"] * item["qtd"] for item in itens), 2)
    desconto = round(subtotal * 0.10, 2) if cupom == "DESC10" else 0.0
    frete = 0.0 if subtotal >= 100 else 15.0
    total = round(subtotal - desconto + frete, 2)
    return {
        "subtotal": subtotal,
        "desconto": desconto,
        "frete": frete,
        "total": total,
    }


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
