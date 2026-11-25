"""Solucao do exercicio 06. Tente resolver o arquivo em exercicios/ antes de abrir."""


def resposta(status: int, dados=None, erro: str | None = None) -> dict:
    corpo: dict = {"status": status, "ok": 200 <= status < 300}
    if dados is not None:
        corpo["dados"] = dados
    if erro is not None:
        corpo["erro"] = erro
    return corpo


def _nome_valido(nome: object) -> str | None:
    if not isinstance(nome, str):
        return None
    limpo = nome.strip()
    return limpo or None


def _preco_valido(preco: object) -> bool:
    return type(preco) in (int, float) and preco > 0


def criar_produto(body: dict, produtos: list[dict]) -> dict:
    nome = _nome_valido(body.get("nome"))
    preco = body.get("preco")
    if nome is None or not _preco_valido(preco):
        return resposta(400, erro="dados invalidos")

    novo_id = max((p["id"] for p in produtos), default=0) + 1
    produto = {"id": novo_id, "nome": nome, "preco": preco, "estoque": 0}
    produtos.append(produto)
    return resposta(201, dados=produto)


def listar_produtos(produtos: list[dict], nome: str | None = None) -> dict:
    if nome is None:
        return resposta(200, dados=list(produtos))
    trecho = nome.lower()
    dados = [p for p in produtos if trecho in p["nome"].lower()]
    return resposta(200, dados=dados)


def buscar_produto(produtos: list[dict], produto_id: int) -> dict:
    for produto in produtos:
        if produto["id"] == produto_id:
            return resposta(200, dados=produto)
    return resposta(404, erro="produto nao encontrado")


def atualizar_estoque(produtos: list[dict], produto_id: int, quantidade: int) -> dict:
    if type(quantidade) is not int or quantidade < 0:
        return resposta(400, erro="dados invalidos")

    for produto in produtos:
        if produto["id"] == produto_id:
            produto["estoque"] = quantidade
            return resposta(200, dados=produto)
    return resposta(404, erro="produto nao encontrado")


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    produtos: list[dict] = []

    criado = criar_produto({"nome": "  Caneta ", "preco": 2.5}, produtos)
    _verificar(criado["status"] == 201 and criado["ok"] is True, "criar devolve 201", falhas)
    _verificar(
        criado.get("dados") == {"id": 1, "nome": "Caneta", "preco": 2.5, "estoque": 0},
        f"produto normalizado, veio {criado.get('dados')}",
        falhas,
    )

    invalido = criar_produto({"nome": "  ", "preco": 2}, produtos)
    _verificar(
        invalido["status"] == 400 and invalido.get("erro") == "dados invalidos",
        "nome vazio",
        falhas,
    )
    _verificar(len(produtos) == 1, "produto invalido nao foi gravado", falhas)

    preco_zero = criar_produto({"nome": "Lapis", "preco": 0}, produtos)
    _verificar(preco_zero["status"] == 400, "preco zero rejeitado", falhas)

    preco_bool = criar_produto({"nome": "Lapis", "preco": True}, produtos)
    _verificar(preco_bool["status"] == 400, "preco bool rejeitado", falhas)

    segundo = criar_produto({"nome": "Lapis", "preco": 1}, produtos)
    _verificar(segundo["dados"]["id"] == 2, "id incremental", falhas)

    lista = listar_produtos(produtos)
    _verificar(len(lista["dados"]) == 2, "lista os dois produtos", falhas)

    filtro = listar_produtos(produtos, nome="CAN")
    _verificar(
        [p["nome"] for p in filtro["dados"]] == ["Caneta"],
        "filtro sem diferenciar maiusculas",
        falhas,
    )

    achou = buscar_produto(produtos, 2)
    _verificar(achou["status"] == 200 and achou["dados"]["nome"] == "Lapis", "busca por id", falhas)

    sumiu = buscar_produto(produtos, 99)
    _verificar(
        sumiu["status"] == 404 and sumiu.get("erro") == "produto nao encontrado",
        "id inexistente",
        falhas,
    )

    atualizado = atualizar_estoque(produtos, 1, 10)
    _verificar(
        atualizado["status"] == 200 and atualizado["dados"]["estoque"] == 10,
        "estoque atualizado",
        falhas,
    )
    _verificar(produtos[0]["estoque"] == 10, "mudanca ficou na lista", falhas)

    ruim = atualizar_estoque(produtos, 1, -1)
    _verificar(ruim["status"] == 400 and produtos[0]["estoque"] == 10, "estoque negativo nao grava", falhas)

    bool_qtd = atualizar_estoque(produtos, 1, False)  # type: ignore[arg-type]
    _verificar(bool_qtd["status"] == 400 and produtos[0]["estoque"] == 10, "bool nao e quantidade", falhas)

    ausente = atualizar_estoque(produtos, 50, 3)
    _verificar(ausente["status"] == 404, "atualizar id inexistente", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
