"""Solucao de pleno/01_conta_bancaria.py. Tente resolver o enunciado antes de abrir."""


class SaldoInsuficiente(Exception):
    pass


def _quantia(valor: float) -> float:
    if isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor <= 0:
        raise ValueError("valor invalido")
    return round(float(valor), 2)


class Conta:
    def __init__(self, numero: str, titular: str, saldo: float = 0):
        if not isinstance(numero, str) or not numero.strip():
            raise ValueError("numero invalido")
        if not isinstance(titular, str) or not titular.strip():
            raise ValueError("titular invalido")
        if isinstance(saldo, bool) or not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("saldo invalido")
        self.numero = numero.strip()
        self.titular = titular.strip()
        self._saldo = round(float(saldo), 2)
        self._extrato: list[dict] = []

    @property
    def saldo(self) -> float:
        return self._saldo

    def _lancar(self, tipo: str, valor: float, **extra) -> None:
        linha = {"tipo": tipo, "valor": valor, "saldo": self._saldo}
        linha.update(extra)
        self._extrato.append(linha)

    def depositar(self, valor: float) -> None:
        quantia = _quantia(valor)
        self._saldo = round(self._saldo + quantia, 2)
        self._lancar("deposito", quantia)

    def sacar(self, valor: float) -> None:
        quantia = _quantia(valor)
        if quantia > self._saldo:
            raise SaldoInsuficiente("saldo insuficiente")
        self._saldo = round(self._saldo - quantia, 2)
        self._lancar("saque", quantia)

    def transferir(self, destino: "Conta", valor: float) -> None:
        if destino is self:
            raise ValueError("conta de destino invalida")
        quantia = _quantia(valor)
        if quantia > self._saldo:
            raise SaldoInsuficiente("saldo insuficiente")
        self._saldo = round(self._saldo - quantia, 2)
        destino._saldo = round(destino._saldo + quantia, 2)
        self._lancar("transferencia_enviada", quantia, conta=destino.numero)
        destino._lancar("transferencia_recebida", quantia, conta=self.numero)

    def extrato(self) -> list[dict]:
        return [dict(linha) for linha in self._extrato]


if __name__ == "__main__":
    from _rodar import rodar

    rodar(SaldoInsuficiente=SaldoInsuficiente, Conta=Conta)
