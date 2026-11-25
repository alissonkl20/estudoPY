"""
Teste tecnico 26 — Cobranca idempotente

Nivel pleno. A mesma chave nao pode cobrar duas vezes. Repetir a mesma
chave com o mesmo valor devolve o estado, sem somar de novo. A mesma
chave com outro valor e erro.

Implemente Caixa.

- saldo comeca em 0
- cobrar(chave, valor) -> {"status": "criado"|"repetido", "saldo": int}
- valor: int > 0 (bool nao vale)
- chave: str nao vazia
- primeira vez: status "criado" e saldo aumenta
- de novo, mesmo valor: status "repetido" e saldo igual
- de novo, outro valor: ValueError e saldo igual

Como testar:
    python3 pleno/26_idempotencia.py
"""


class Caixa:
    def __init__(self) -> None:
        self.saldo = 0

    def cobrar(self, chave: str, valor: int) -> dict:
        return {"status": "", "saldo": self.saldo}


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    caixa = Caixa()
    _verificar(
        caixa.cobrar("k1", 10) == {"status": "criado", "saldo": 10},
        "primeira cobranca",
        falhas,
    )
    _verificar(
        caixa.cobrar("k1", 10) == {"status": "repetido", "saldo": 10},
        "repetir nao soma",
        falhas,
    )
    try:
        caixa.cobrar("k1", 5)
        _verificar(False, "mesmo id com outro valor deveria falhar", falhas)
    except ValueError:
        _verificar(caixa.saldo == 10, "erro nao altera o saldo", falhas)

    _verificar(caixa.cobrar("k2", 5)["saldo"] == 15, "outra chave soma", falhas)

    try:
        caixa.cobrar("k3", True)  # type: ignore[arg-type]
        _verificar(False, "bool nao e valor", falhas)
    except ValueError:
        _verificar(caixa.saldo == 15, "bool nao credita", falhas)

    try:
        caixa.cobrar("", 1)
        _verificar(False, "chave vazia deveria falhar", falhas)
    except ValueError:
        _verificar(True, "chave vazia levanta ValueError", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
