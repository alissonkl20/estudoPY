"""Solucao de pleno/21_versoes.py. Tente resolver o enunciado antes de abrir."""


def _partes(versao: str) -> tuple[int, ...]:
    if not isinstance(versao, str) or not versao or versao.startswith(".") or versao.endswith("."):
        raise ValueError("versao invalida")
    numeros = []
    for parte in versao.split("."):
        if not parte.isdigit():
            raise ValueError("versao invalida")
        numeros.append(int(parte))
    return tuple(numeros)


def _alinhar(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    tamanho = max(len(a), len(b))
    return a + (0,) * (tamanho - len(a)), b + (0,) * (tamanho - len(b))


def comparar(a: str, b: str) -> int:
    esquerda, direita = _alinhar(_partes(a), _partes(b))
    if esquerda < direita:
        return -1
    if esquerda > direita:
        return 1
    return 0


def ordenar(versoes: list[str]) -> list[str]:
    partes = [_partes(versao) for versao in versoes]
    tamanho = max((len(parte) for parte in partes), default=0)
    chaves = [parte + (0,) * (tamanho - len(parte)) for parte in partes]
    return [versao for _, versao in sorted(zip(chaves, list(versoes)))]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(comparar=comparar, ordenar=ordenar)
