"""Solucao de pleno/26_idempotencia.py. Tente resolver o enunciado antes de abrir."""


class Caixa:
    def __init__(self) -> None:
        self.saldo = 0
        self._chaves: dict[str, int] = {}

    def cobrar(self, chave: str, valor: int) -> dict:
        if not isinstance(chave, str) or chave == "":
            raise ValueError("chave invalida")
        if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
            raise ValueError("valor invalido")
        if chave in self._chaves:
            if self._chaves[chave] != valor:
                raise ValueError("chave reutilizada com outro valor")
            return {"status": "repetido", "saldo": self.saldo}
        self.saldo += valor
        self._chaves[chave] = valor
        return {"status": "criado", "saldo": self.saldo}


if __name__ == "__main__":
    from _rodar import rodar

    rodar(Caixa=Caixa)
