"""Solucao de logica/02_anagramas.py. Tente resolver o enunciado antes de abrir."""


def _chave(texto: str) -> str:
    return "".join(sorted("".join(texto.lower().split())))


def sao_anagramas(a: str, b: str) -> bool:
    return _chave(a) == _chave(b)


def agrupar(palavras: list[str]) -> list[list[str]]:
    grupos: dict[str, list[str]] = {}
    ordem: list[str] = []
    for palavra in palavras:
        chave = _chave(palavra)
        if chave not in grupos:
            grupos[chave] = []
            ordem.append(chave)
        grupos[chave].append(palavra)
    return [grupos[chave] for chave in ordem]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(sao_anagramas=sao_anagramas, agrupar=agrupar)
