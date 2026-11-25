"""Solucao de pleno/17_arvore_categorias.py. Tente resolver o enunciado antes de abrir."""


def _achar(no: dict, nome: str, trilha: list[str]):
    atual = trilha + [no["nome"]]
    if no["nome"] == nome:
        return no, atual
    for filho in no.get("filhos") or []:
        achou = _achar(filho, nome, atual)
        if achou is not None:
            return achou
    return None


def caminho(arvore: dict, nome: str) -> list[str] | None:
    achou = _achar(arvore, nome, [])
    if achou is None:
        return None
    return achou[1]


def descendentes(arvore: dict, nome: str) -> list[str] | None:
    achou = _achar(arvore, nome, [])
    if achou is None:
        return None
    saida: list[str] = []

    def visitar(no: dict) -> None:
        for filho in no.get("filhos") or []:
            saida.append(filho["nome"])
            visitar(filho)

    visitar(achou[0])
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(caminho=caminho, descendentes=descendentes)
