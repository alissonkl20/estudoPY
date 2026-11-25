"""
Teste tecnico 12 — Dinheiro com centavos exatos

Nivel pleno. float erra conta de centavos. Use decimal.Decimal,
com duas casas e arredondamento half up (meio centavo sobe).

Implemente a classe Dinheiro.

- aceita str ou int. int e em reais: 2 vira 2.00
- rejeita float e bool com ValueError
- rejeita valor negativo
- "1.005" vira 1.01; "10.555" vira 10.56
- soma e subtracao devolvem outro Dinheiro e nao mudam os operandos
- subtracao que ficaria negativa levanta ValueError
- str sempre com duas casas: "10.50"
- dois Dinheiro com o mesmo valor sao iguais
- repartir(n) divide em n partes. O resto dos centavos vai para as
  primeiras partes. A soma das partes e o valor original
- n < 1, ou bool, levanta ValueError

Como testar:
    python3 pleno/12_dinheiro.py
"""


class Dinheiro:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro: "Dinheiro") -> "Dinheiro":
        return self

    def __sub__(self, outro: "Dinheiro") -> "Dinheiro":
        return self

    def __eq__(self, outro: object) -> bool:
        return False

    def repartir(self, partes: int) -> list["Dinheiro"]:
        return []

    def __str__(self) -> str:
        return ""


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []

    _verificar(str(Dinheiro("10.5")) == "10.50", "uma casa vira duas", falhas)
    _verificar(str(Dinheiro(2)) == "2.00", "int e reais inteiros", falhas)
    _verificar(str(Dinheiro("1.005")) == "1.01", "meio centavo sobe", falhas)
    _verificar(str(Dinheiro("10.555")) == "10.56", "half up", falhas)
    _verificar(Dinheiro("10.50") == Dinheiro("10.5"), "igualdade pelo valor", falhas)

    soma = Dinheiro("10.50") + Dinheiro("0.50")
    _verificar(soma == Dinheiro("11"), f"soma, veio {soma}", falhas)

    origem = Dinheiro("5.00")
    try:
        origem - Dinheiro("8")
        _verificar(False, "subtracao negativa deveria falhar", falhas)
    except ValueError:
        _verificar(str(origem) == "5.00", "operando nao muda", falhas)

    partes = Dinheiro("1").repartir(3)
    _verificar(
        [str(parte) for parte in partes] == ["0.34", "0.33", "0.33"],
        f"reparte o centavo extra, veio {partes}",
        falhas,
    )
    if len(partes) == 3:
        total = partes[0] + partes[1] + partes[2]
        _verificar(total == Dinheiro("1"), "soma das partes fecha", falhas)
    else:
        _verificar(False, "soma das partes fecha", falhas)

    miudo = Dinheiro("0.02").repartir(3)
    _verificar(
        [str(parte) for parte in miudo] == ["0.01", "0.01", "0.00"],
        f"pode sobrar zero, veio {miudo}",
        falhas,
    )

    for ruim in (1.5, True, "-1", "abc"):
        try:
            Dinheiro(ruim)
            _verificar(False, f"{ruim!r} deveria ser rejeitado", falhas)
        except ValueError:
            _verificar(True, f"{ruim!r} levanta ValueError", falhas)

    try:
        Dinheiro("1").repartir(0)
        _verificar(False, "zero partes deveria falhar", falhas)
    except ValueError:
        _verificar(True, "zero partes levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
