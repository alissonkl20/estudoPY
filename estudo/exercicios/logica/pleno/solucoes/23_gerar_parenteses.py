"""Solucao de logica/pleno/23_gerar_parenteses.py. Tente resolver o enunciado antes de abrir."""

def gerar_parenteses(n: int) -> list[str]:
    if n < 1:
        raise ValueError("n invalido")
    saida = []

    def montar(aberto: int, fechado: int, atual: str) -> None:
        if len(atual) == 2 * n:
            saida.append(atual)
            return
        if aberto < n:
            montar(aberto + 1, fechado, atual + "(")
        if fechado < aberto:
            montar(aberto, fechado + 1, atual + ")")

    montar(0, 0, "")
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(gerar_parenteses=gerar_parenteses)
