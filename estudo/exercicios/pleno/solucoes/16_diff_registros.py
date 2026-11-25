"""Solucao de pleno/16_diff_registros.py. Tente resolver o enunciado antes de abrir."""


def _indexar(registros: list[dict]) -> dict:
    indice = {}
    for registro in registros:
        if "id" not in registro:
            raise ValueError("registro sem id")
        ident = registro["id"]
        if ident in indice:
            raise ValueError("id duplicado")
        indice[ident] = registro
    return indice


def diff(antes: list[dict], depois: list[dict]) -> dict:
    origem = _indexar(antes)
    destino = _indexar(depois)
    adicionados = [ident for ident in destino if ident not in origem]
    removidos = [ident for ident in origem if ident not in destino]
    alterados = [
        ident
        for ident in destino
        if ident in origem and destino[ident] != origem[ident]
    ]
    return {
        "adicionados": adicionados,
        "removidos": removidos,
        "alterados": alterados,
    }


if __name__ == "__main__":
    from _rodar import rodar

    rodar(diff=diff)
