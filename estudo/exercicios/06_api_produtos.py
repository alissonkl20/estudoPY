"""
Exercicio 06 — Mini API de produtos em memoria

Aqui nao tem framework. A lista `produtos` faz o papel do banco,
e cada funcao faz o papel de uma rota.

resposta() ja monta o JSON. Implemente as quatro rotas.

Produto gravado:
    {"id": int, "nome": str, "preco": numero, "estoque": int}

criar_produto(body, produtos)
- nome: str que, depois do strip, nao fica vazia. Grave o nome sem espacos nas pontas.
- preco: int ou float maior que 0 (bool nao vale)
- estoque inicial: 0
- id: 1 se a lista estiver vazia, senao o maior id + 1
- sucesso: status 201 e o produto em "dados"
- erro: status 400 e erro "dados invalidos" (nao grave o produto)

listar_produtos(produtos, nome=None)
- status 200
- nome None devolve todos
- nome filtra por trecho, sem diferenciar maiusculas ("can" acha "Caneta")

buscar_produto(produtos, produto_id)
- achou: status 200 e o produto
- nao achou: status 404 e erro "produto nao encontrado"

atualizar_estoque(produtos, produto_id, quantidade)
- quantidade: int maior ou igual a 0 (bool nao vale)
- achou e quantidade valida: altera o produto na lista e devolve status 200
- quantidade invalida: status 400, erro "dados invalidos", estoque nao muda
- id inexistente: status 404, erro "produto nao encontrado"

Como testar:
    python3 exercicios/06_api_produtos.py
"""


def resposta(status: int, dados=None, erro: str | None = None) -> dict:
    corpo: dict = {"status": status, "ok": 200 <= status < 300}
    if dados is not None:
        corpo["dados"] = dados
    if erro is not None:
        corpo["erro"] = erro
    return corpo


def criar_produto(body: dict, produtos: list[dict]) -> dict:
    # seu codigo aqui
    return resposta(500, erro="nao implementado")


def listar_produtos(produtos: list[dict], nome: str | None = None) -> dict:
    # seu codigo aqui
    return resposta(500, erro="nao implementado")


def buscar_produto(produtos: list[dict], produto_id: int) -> dict:
    # seu codigo aqui
    return resposta(500, erro="nao implementado")


def atualizar_estoque(produtos: list[dict], produto_id: int, quantidade: int) -> dict:
    # seu codigo aqui
    return resposta(500, erro="nao implementado")


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
