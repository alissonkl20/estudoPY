"""Solucao do exercicio 03. Tente resolver o arquivo em exercicios/ antes de abrir."""


def filtrar_pedidos(
    pedidos: list[dict],
    status: str | None = None,
    valor_min: float | None = None,
    ordenar_por: str = "id",
) -> list[dict]:
    resultado = []
    for pedido in pedidos:
        if status is not None and pedido["status"] != status:
            continue
        if valor_min is not None and pedido["valor"] < valor_min:
            continue
        resultado.append(pedido)
    return sorted(resultado, key=lambda pedido: pedido[ordenar_por])


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
