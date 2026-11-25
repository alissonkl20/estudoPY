"""Solucao de pleno/04_geradores.py. Tente resolver o enunciado antes de abrir."""


def lotes(itens, tamanho: int):
    if isinstance(tamanho, bool) or not isinstance(tamanho, int) or tamanho < 1:
        raise ValueError("tamanho invalido")
    lote = []
    for item in itens:
        lote.append(item)
        if len(lote) == tamanho:
            yield lote
            lote = []
    if lote:
        yield lote


def filtrar_linhas(linhas):
    for linha in linhas:
        limpa = linha.strip()
        if not limpa or limpa.startswith("#"):
            continue
        yield limpa


if __name__ == "__main__":
    from _rodar import rodar

    rodar(lotes=lotes, filtrar_linhas=filtrar_linhas)
