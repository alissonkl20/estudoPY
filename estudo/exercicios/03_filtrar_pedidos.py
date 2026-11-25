"""
Exercicio 03 — Filtrar e ordenar pedidos

Um endpoint GET /pedidos recebe filtros opcionais e um campo de ordenacao.
A funcao pura abaixo e o miolo dessa rota.

Implemente filtrar_pedidos(pedidos, status=None, valor_min=None, ordenar_por="id").

Regras:
- status None significa "qualquer status"
- valor_min None significa "qualquer valor"
- valor_min e inclusivo: pedido com valor igual entra
- ordenar_por e a chave do dicionario ("id" ou "valor")
- devolva uma lista nova
- nao altere a ordem nem o conteudo da lista recebida

Como testar:
    python3 exercicios/03_filtrar_pedidos.py
"""


def filtrar_pedidos(
    pedidos: list[dict],
    status: str | None = None,
    valor_min: float | None = None,
    ordenar_por: str = "id",
) -> list[dict]:
    # seu codigo aqui
    return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


PEDIDOS = [
    {"id": 1, "status": "pago", "valor": 50, "cliente": "Ana"},
    {"id": 2, "status": "pendente", "valor": 120, "cliente": "Bruno"},
    {"id": 3, "status": "pago", "valor": 80, "cliente": "Caio"},
    {"id": 4, "status": "cancelado", "valor": 200, "cliente": "Duda"},
]


def testar() -> None:
    falhas: list[str] = []
    original = [dict(p) for p in PEDIDOS]

    pagos = filtrar_pedidos(PEDIDOS, status="pago")
    _verificar([p["id"] for p in pagos] == [1, 3], f"so pagos, veio {pagos}", falhas)

    caros = filtrar_pedidos(PEDIDOS, valor_min=120)
    _verificar([p["id"] for p in caros] == [2, 4], "valor minimo inclusivo", falhas)

    pagos_caros = filtrar_pedidos(PEDIDOS, status="pago", valor_min=60)
    _verificar([p["id"] for p in pagos_caros] == [3], "status e valor juntos", falhas)

    por_valor = filtrar_pedidos(PEDIDOS, status="pago", ordenar_por="valor")
    _verificar([p["id"] for p in por_valor] == [1, 3], "pagos ordenados por valor", falhas)

    _verificar(
        filtrar_pedidos(PEDIDOS, status="enviado") == [],
        "filtro sem resultado",
        falhas,
    )
    _verificar(PEDIDOS == original, "lista original intacta", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
