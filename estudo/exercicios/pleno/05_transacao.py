"""
Teste tecnico 05 — Transacao em memoria

Nivel pleno. O bloco with ou confirma tudo, ou desfaz tudo.
Valores aninhados (dict e list) tambem voltam atras. Use copia profunda.

Implemente BancoMemoria e o context manager transacao(banco).

- BancoMemoria(dados=None) guarda uma copia dos dados, nao o dict original
- sem excecao: as mudancas ficam
- com excecao: restaura o estado de antes do with e deixa a excecao subir
- trocar banco.dados por outro dict tambem desfaz

Como testar:
    python3 pleno/05_transacao.py
"""

from contextlib import contextmanager


class BancoMemoria:
    def __init__(self, dados: dict | None = None):
        # seu codigo aqui
        self.dados = {} if dados is None else dados


@contextmanager
def transacao(banco: BancoMemoria):
    # seu codigo aqui
    yield banco


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def testar() -> None:
    falhas: list[str] = []
    origem = {"a": 1, "interno": {"n": 1}}
    banco = BancoMemoria(origem)
    origem["a"] = 99
    _verificar(banco.dados["a"] == 1, "construtor copia os dados", falhas)

    with transacao(banco):
        banco.dados["a"] = 2
        banco.dados["b"] = 3
        banco.dados["interno"]["n"] = 8
    _verificar(
        banco.dados == {"a": 2, "b": 3, "interno": {"n": 8}},
        "commit mantem a mudanca",
        falhas,
    )

    try:
        with transacao(banco):
            banco.dados["a"] = 9
            banco.dados["interno"]["n"] = 0
            banco.dados["novo"] = [1]
            raise RuntimeError("falhou")
    except RuntimeError:
        _verificar(
            banco.dados == {"a": 2, "b": 3, "interno": {"n": 8}},
            "rollback de dict aninhado",
            falhas,
        )
    else:
        _verificar(False, "RuntimeError deveria subir", falhas)

    try:
        with transacao(banco):
            banco.dados = {"z": 1}
            raise RuntimeError("troca")
    except RuntimeError:
        _verificar("a" in banco.dados and banco.dados["a"] == 2, "desfaz troca do dict", falhas)

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
