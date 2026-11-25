"""Solucao de junior/07_troco.py. Tente resolver o enunciado antes de abrir."""

_MOEDAS = (100, 50, 25, 10, 5, 1)


def troco(centavos: int) -> dict:
    if isinstance(centavos, bool) or not isinstance(centavos, int) or centavos < 0:
        raise ValueError("centavos invalido")
    resultado = {}
    restante = centavos
    for moeda in _MOEDAS:
        quantidade, restante = divmod(restante, moeda)
        resultado[moeda] = quantidade
    return resultado


if __name__ == "__main__":
    from _rodar import rodar

    rodar(troco=troco)
