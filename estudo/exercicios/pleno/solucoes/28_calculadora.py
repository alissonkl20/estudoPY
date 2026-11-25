"""Solucao de pleno/28_calculadora.py. Tente resolver o enunciado antes de abrir."""


def _tokenizar(expressao: str) -> list[str]:
    if not isinstance(expressao, str):
        raise ValueError("expressao invalida")
    tokens: list[str] = []
    indice = 0
    while indice < len(expressao):
        caractere = expressao[indice]
        if caractere.isspace():
            indice += 1
            continue
        if caractere in "+-*()":
            tokens.append(caractere)
            indice += 1
            continue
        if caractere.isdigit():
            fim = indice + 1
            while fim < len(expressao) and expressao[fim].isdigit():
                fim += 1
            tokens.append(expressao[indice:fim])
            indice = fim
            continue
        raise ValueError("expressao invalida")
    return tokens


def calcular(expressao: str) -> int:
    tokens = _tokenizar(expressao)
    if not tokens:
        raise ValueError("expressao invalida")
    posicao = 0

    def olhar():
        if posicao >= len(tokens):
            return None
        return tokens[posicao]

    def consumir(esperado: str | None = None) -> str:
        nonlocal posicao
        token = olhar()
        if token is None or (esperado is not None and token != esperado):
            raise ValueError("expressao invalida")
        posicao += 1
        return token

    def expressao_soma() -> int:
        valor = termo()
        while olhar() in ("+", "-"):
            operador = consumir()
            direita = termo()
            valor = valor + direita if operador == "+" else valor - direita
        return valor

    def termo() -> int:
        valor = fator()
        while olhar() == "*":
            consumir("*")
            valor *= fator()
        return valor

    def fator() -> int:
        token = olhar()
        if token == "(":
            consumir("(")
            valor = expressao_soma()
            consumir(")")
            return valor
        if token is None or not token.isdigit():
            raise ValueError("expressao invalida")
        return int(consumir())

    resultado = expressao_soma()
    if posicao != len(tokens):
        raise ValueError("expressao invalida")
    return resultado


if __name__ == "__main__":
    from _rodar import rodar

    rodar(calcular=calcular)
