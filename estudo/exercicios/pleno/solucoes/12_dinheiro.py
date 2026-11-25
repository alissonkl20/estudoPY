"""Solucao de pleno/12_dinheiro.py. Tente resolver o enunciado antes de abrir."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

_CENTAVO = Decimal("0.01")


def _para_decimal(valor) -> Decimal:
    if isinstance(valor, bool) or isinstance(valor, float):
        raise ValueError("valor invalido")
    if isinstance(valor, Decimal):
        numero = valor
    elif isinstance(valor, int):
        numero = Decimal(valor)
    elif isinstance(valor, str):
        texto = valor.strip()
        if not texto or "e" in texto.lower() or "," in texto:
            raise ValueError("valor invalido")
        try:
            numero = Decimal(texto)
        except InvalidOperation as erro:
            raise ValueError("valor invalido") from erro
    else:
        raise ValueError("valor invalido")
    if not numero.is_finite():
        raise ValueError("valor invalido")
    quantizado = numero.quantize(_CENTAVO, rounding=ROUND_HALF_UP)
    if quantizado < 0:
        raise ValueError("valor invalido")
    return quantizado


class Dinheiro:
    def __init__(self, valor):
        self._valor = _para_decimal(valor)

    def __add__(self, outro: "Dinheiro") -> "Dinheiro":
        if not isinstance(outro, Dinheiro):
            return NotImplemented
        return Dinheiro(self._valor + outro._valor)

    def __sub__(self, outro: "Dinheiro") -> "Dinheiro":
        if not isinstance(outro, Dinheiro):
            return NotImplemented
        resultado = self._valor - outro._valor
        if resultado < 0:
            raise ValueError("valor insuficiente")
        return Dinheiro(resultado)

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Dinheiro):
            return NotImplemented
        return self._valor == outro._valor

    def repartir(self, partes: int) -> list["Dinheiro"]:
        if isinstance(partes, bool) or not isinstance(partes, int) or partes < 1:
            raise ValueError("partes invalida")
        centavos = int((self._valor * 100).to_integral_value())
        base, resto = divmod(centavos, partes)
        saida = []
        for indice in range(partes):
            quantia = base + (1 if indice < resto else 0)
            saida.append(Dinheiro(Decimal(quantia) / Decimal(100)))
        return saida

    def __str__(self) -> str:
        return f"{self._valor:.2f}"


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Dinheiro=Dinheiro)
