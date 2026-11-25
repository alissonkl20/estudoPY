"""
Teste tecnico 01 — Conta bancaria

Nivel pleno. Modele a conta com invariantes: saldo nunca fica negativo,
operacao invalida nao grava extrato, e transferencia e atomica.

Implemente a excecao SaldoInsuficiente e a classe Conta.

Conta(numero, titular, saldo=0)
- numero e titular: str nao vazia depois do strip; grave sem espacos nas pontas
- saldo inicial: int ou float >= 0 (bool nao vale). Nao gera linha de extrato
- propriedade saldo, sem setter

depositar(valor) e sacar(valor)
- valor: int ou float > 0 (bool nao vale); senao ValueError
- sacar acima do saldo: SaldoInsuficiente, saldo e extrato intactos

transferir(destino, valor)
- destino precisa ser outra Conta; transferir para si levanta ValueError
- sem saldo: SaldoInsuficiente e nenhuma das duas contas muda
- origem ganha tipo "transferencia_enviada"
- destino ganha tipo "transferencia_recebida"
- o campo "conta" guarda o numero da outra conta

Cada linha do extrato:
    {"tipo": str, "valor": float, "saldo": float}
Transferencia tambem tem "conta".
Valores com 2 casas (round). extrato() devolve copia: mudar a lista ou o
dicionario devolvido nao altera a conta.

Como testar:
    python3 pleno/01_conta_bancaria.py
"""


class SaldoInsuficiente(Exception):
    pass


class Conta:
    def __init__(self, numero: str, titular: str, saldo: float = 0):
        # seu codigo aqui
        self.numero = numero
        self.titular = titular

    @property
    def saldo(self) -> float:
        # seu codigo aqui
        return 0.0

    def depositar(self, valor: float) -> None:
        # seu codigo aqui
        return None

    def sacar(self, valor: float) -> None:
        # seu codigo aqui
        return None

    def transferir(self, destino: "Conta", valor: float) -> None:
        # seu codigo aqui
        return None

    def extrato(self) -> list[dict]:
        # seu codigo aqui
        return []


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    ana = Conta(" 1 ", " Ana ", 0)
    bruno = Conta("2", "Bruno")

    _verificar(ana.numero == "1" and ana.titular == "Ana", "strip no construtor", falhas)
    ana.depositar(100)
    ana.sacar(40)
    ana.transferir(bruno, 10)

    _verificar(ana.saldo == 50.0, f"saldo da origem, veio {ana.saldo}", falhas)
    _verificar(bruno.saldo == 10.0, f"saldo do destino, veio {bruno.saldo}", falhas)
    _verificar(
        ana.extrato()
        == [
            {"tipo": "deposito", "valor": 100.0, "saldo": 100.0},
            {"tipo": "saque", "valor": 40.0, "saldo": 60.0},
            {
                "tipo": "transferencia_enviada",
                "valor": 10.0,
                "saldo": 50.0,
                "conta": "2",
            },
        ],
        "extrato da origem",
        falhas,
    )
    _verificar(
        bruno.extrato()
        == [
            {
                "tipo": "transferencia_recebida",
                "valor": 10.0,
                "saldo": 10.0,
                "conta": "1",
            }
        ],
        "extrato do destino",
        falhas,
    )

    copia = ana.extrato()
    copia.append({"tipo": "hack"})
    copia[0]["valor"] = 0
    _verificar(
        len(ana.extrato()) == 3 and ana.extrato()[0]["valor"] == 100.0,
        "extrato devolvido e copia",
        falhas,
    )

    try:
        ana.saldo = 999  # type: ignore[misc]
        _verificar(False, "saldo nao pode ser atribuido", falhas)
    except AttributeError:
        _verificar(True, "saldo sem setter", falhas)

    saldo_antes = ana.saldo
    linhas = len(ana.extrato())
    try:
        ana.sacar(1000)
        _verificar(False, "saque alto deveria falhar", falhas)
    except SaldoInsuficiente:
        _verificar(
            ana.saldo == saldo_antes and len(ana.extrato()) == linhas,
            "saque invalido nao grava",
            falhas,
        )

    try:
        ana.transferir(ana, 1)
        _verificar(False, "transferir para si deveria falhar", falhas)
    except ValueError:
        _verificar(ana.saldo == saldo_antes, "autotransferencia nao mexe no saldo", falhas)

    try:
        ana.depositar(True)  # type: ignore[arg-type]
        _verificar(False, "bool nao e valor", falhas)
    except ValueError:
        _verificar(True, "deposito bool levanta ValueError", falhas)

    try:
        Conta("3", "Caio", -1)
        _verificar(False, "saldo inicial negativo deveria falhar", falhas)
    except ValueError:
        _verificar(True, "saldo inicial negativo levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
