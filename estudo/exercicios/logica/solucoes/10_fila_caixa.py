"""Solucao de logica/10_fila_caixa.py. Tente resolver o enunciado antes de abrir."""


def esperas(clientes: list[dict]) -> list[int]:
    livre = 0
    chegada_anterior = None
    resultado: list[int] = []
    for cliente in clientes:
        chegada = cliente["chegada"]
        duracao = cliente["duracao"]
        if isinstance(chegada, bool) or not isinstance(chegada, int) or chegada < 0:
            raise ValueError("chegada invalida")
        if isinstance(duracao, bool) or not isinstance(duracao, int) or duracao < 1:
            raise ValueError("duracao invalida")
        if chegada_anterior is not None and chegada < chegada_anterior:
            raise ValueError("clientes fora de ordem")
        chegada_anterior = chegada
        inicio = chegada if chegada > livre else livre
        resultado.append(inicio - chegada)
        livre = inicio + duracao
    return resultado


if __name__ == "__main__":
    from _rodar import rodar

    rodar(esperas=esperas)
