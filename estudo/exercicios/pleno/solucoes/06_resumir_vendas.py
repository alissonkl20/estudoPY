"""Solucao de pleno/06_resumir_vendas.py. Tente resolver o enunciado antes de abrir."""


def resumir(vendas: list[dict]) -> list[dict]:
    grupos: dict[str, dict] = {}
    for venda in vendas:
        if venda.get("status") != "paga":
            continue
        valor = venda.get("valor")
        if isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("valor invalido")
        nome = venda["vendedor"]
        grupo = grupos.get(nome)
        if grupo is None:
            grupo = {"vendedor": nome, "total": 0.0, "quantidade": 0}
            grupos[nome] = grupo
        grupo["total"] += float(valor)
        grupo["quantidade"] += 1

    saida = []
    for grupo in grupos.values():
        total = round(grupo["total"], 2)
        quantidade = grupo["quantidade"]
        saida.append(
            {
                "vendedor": grupo["vendedor"],
                "total": total,
                "quantidade": quantidade,
                "ticket_medio": round(total / quantidade, 2),
            }
        )
    saida.sort(key=lambda item: (-item["total"], item["vendedor"]))
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(resumir=resumir)
