"""Solucao de junior/09_compras.py. Tente resolver o enunciado antes de abrir."""


def consolidar(itens: list[dict]) -> list[dict]:
    totais: dict[str, int] = {}
    ordem: list[str] = []
    for item in itens:
        nome = item.get("nome")
        qtd = item.get("qtd")
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("nome invalido")
        if isinstance(qtd, bool) or not isinstance(qtd, int) or qtd < 1:
            raise ValueError("quantidade invalida")
        nome = nome.strip()
        if nome not in totais:
            ordem.append(nome)
            totais[nome] = 0
        totais[nome] += qtd
    return [{"nome": nome, "qtd": totais[nome]} for nome in ordem]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(consolidar=consolidar)
