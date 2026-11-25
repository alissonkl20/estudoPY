"""
Teste tecnico 10 — Maquina de estados do pedido

Nivel pleno. O pedido so muda de estado pelas transicoes permitidas.
Transicao ilegal levanta TransicaoInvalida e nao mexe em estado nem historico.

Implemente TransicaoInvalida e Pedido.

Estados e acoes:
- rascunho  -> confirmar -> confirmado
- rascunho  -> cancelar  -> cancelado
- confirmado -> pagar    -> pago
- confirmado -> cancelar -> cancelado
- pago      -> enviar    -> enviado
- enviado e cancelado nao tem saida

historico comeca com ["rascunho"] e ganha o estado novo so quando a acao vale.

Como testar:
    python3 pleno/10_pedido_estados.py
"""


class TransicaoInvalida(Exception):
    pass


class Pedido:
    def __init__(self) -> None:
        self.estado = "rascunho"
        self.historico = ["rascunho"]

    def confirmar(self) -> None:
        # seu codigo aqui
        return None

    def pagar(self) -> None:
        # seu codigo aqui
        return None

    def enviar(self) -> None:
        # seu codigo aqui
        return None

    def cancelar(self) -> None:
        # seu codigo aqui
        return None


def _verificar(condicao: bool, mensagem: str, falhas: list[str]) -> None:
    if condicao:
        print(f"  ok  {mensagem}")
    else:
        print(f"  FALHOU  {mensagem}")
        falhas.append(mensagem)


def _proibida(pedido: Pedido, acao: str, falhas: list[str]) -> None:
    estado = pedido.estado
    historico = list(pedido.historico)
    try:
        getattr(pedido, acao)()
        _verificar(False, f"{acao} a partir de {estado} deveria falhar", falhas)
    except TransicaoInvalida:
        _verificar(
            pedido.estado == estado and pedido.historico == historico,
            f"{acao} ilegal a partir de {estado} nao grava",
            falhas,
        )


def testar() -> None:
    falhas: list[str] = []
    pedido = Pedido()
    pedido.confirmar()
    pedido.pagar()
    pedido.enviar()
    _verificar(pedido.estado == "enviado", f"fluxo feliz, estado {pedido.estado}", falhas)
    _verificar(
        pedido.historico == ["rascunho", "confirmado", "pago", "enviado"],
        f"historico, veio {pedido.historico}",
        falhas,
    )
    _proibida(pedido, "cancelar", falhas)

    cancelado = Pedido()
    cancelado.cancelar()
    _verificar(cancelado.estado == "cancelado", "cancela rascunho", falhas)
    _proibida(cancelado, "confirmar", falhas)

    pago = Pedido()
    pago.confirmar()
    pago.pagar()
    _proibida(pago, "cancelar", falhas)
    _proibida(pago, "confirmar", falhas)

    confirmado = Pedido()
    confirmado.confirmar()
    confirmado.cancelar()
    _verificar(
        confirmado.historico == ["rascunho", "confirmado", "cancelado"],
        "cancela depois de confirmar",
        falhas,
    )

    if falhas:
        print(f"\n{len(falhas)} teste(s) falharam.")
    else:
        print("\nTodos os testes passaram.")


if __name__ == "__main__":
    testar()
