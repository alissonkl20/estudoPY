"""Solucao de pleno/22_sobrepor_config.py. Tente resolver o enunciado antes de abrir."""

import copy


def _misturar(destino: dict, camada: dict) -> None:
    for chave, valor in camada.items():
        if isinstance(valor, dict) and isinstance(destino.get(chave), dict):
            _misturar(destino[chave], valor)
        else:
            destino[chave] = copy.deepcopy(valor)


def sobrepor(base: dict, *camadas: dict) -> dict:
    resultado = copy.deepcopy(base)
    for camada in camadas:
        _misturar(resultado, camada)
    return resultado


if __name__ == "__main__":
    from _rodar import rodar

    rodar(sobrepor=sobrepor)
